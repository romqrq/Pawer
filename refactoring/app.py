# Importing libraries
import os
from os import path
from flask import Flask, flash, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if path.exists('env.py'):
    import env

# Creating instance of Flask
APP = Flask(__name__)
APP.secret_key = os.environ.get('SECRET_KEY')

# Adding Mongo database name and URI linking to that database.
APP.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
APP.config["MONGO_URI"] = os.environ.get('MONGO_URI')

# Creating an instance of PyMongo
MONGO = PyMongo(APP)

# Importing helper functions
import refactoring.app_functions as app_functions


@APP.route('/')
def user_home():
    """ Main page where users can choose where to go"""
    return render_template('pages/index.html')


@APP.route('/register')
def register():
    """ Page where users can choose a type of account and
     register through the specific form"""
    return render_template('pages/register.html')


@APP.route('/login', methods=['GET', 'POST'])
def user_login():
    """ Loads page where users can login, checks the email and password on the
     database. If the user is valid, variables are added to session to be used
    to adjust the content to the type of user and privileges """

    if request.method == 'POST':
        app_functions.check_user_on_login(request.form['password'], request.form['login_email'])

    return render_template('pages/login.html')


@APP.route('/logout', methods=['GET', 'POST'])
def user_logout():
    """ Simplified logout function that removes items added to the session
    list during login """

    session.clear()

    flash('You have been logged out successfully.', 'info')
    return render_template('pages/index.html')

# DASHBOARD
@APP.route('/dashboard', methods=['GET', 'POST'])
def get_dashboard():
    """ Function to load the dashboard where users can update their account
    details or delete their account."""
    return render_template('pages/dashboard.html',
                           user=MONGO.db.users.find_one(
                               {'_id': ObjectId(session['user_id'])}))

# CREATE
# Add entry
@APP.route('/add/<usr_type>', methods=['POST'])
def add_entry(usr_type):
    """ Function to create new entry in the users database collection. It looks up
    for pre-existing records and only adds to database if the record doesn't exist.
    """
    # User or dog exists?
    app_functions.get_existing_user_or_dog(usr_type, request.form)

    # Create user or dog to database
    app_functions.create_user_or_dog(library = usr_type, submitted_form = request.form)

    # Add feedback key to services and stores
    if usr_type == 'services' or usr_type == 'stores':
        app_functions.update_feedback_key_to_user(request.form.to_dict())

    # Update staff status on users
    if usr_type != 'dogs':
        app_functions.update_staff_status_and_user_type_on_user(usr_type, request.form.to_dict())
    
    # Confirmation message and redirect to home page
    flash('You have been successfully registered! Welcome!', 'info')
    return redirect(url_for('user_home'))

# Adopt a dog
@APP.route('/adopt/<usr_id>/<dog_id>', methods=['GET', 'POST'])
def adopt_dog(usr_id, dog_id):
    """ Function to create new entry in the adoptRequest collection.
    It gets information from the adoptant and the dog to create a single
    file."""

    # Adoption request exists?
    app_functions.get_existing_adoption_request(usr_id)

    # Build adoption request to match database
    adopt_req = app_functions.build_adoption_request(usr_id, dog_id, request.form.to_dict())
    
    # Create new adoption request
    app_functions.create_adoption_request(adopt_req)

    # Confirmation message and redirect
    flash('Thank you! Your adoption request was successful. We\'ll be in touch soon!', 'info')
    return redirect(url_for('get_dogs'))


# READ
@APP.route('/requests', methods=['GET', 'POST'])
def get_adopt_requests():
    """ Function to list adoption requests in the database """
    return render_template('pages/requests.html',
                           requests=MONGO.db.adoptRequest.find())

# Find dog
@APP.route('/dogs', methods=['GET', 'POST'])
def get_dogs():
    """ Function to list dogs contained in the database """
    return render_template('pages/dogs.html', dogs=MONGO.db.dogs.find())

# Find user
@APP.route('/users')
def get_users():
    """ Function to list users contained in the database """
    return render_template('pages/users.html',
                           users=MONGO.db.users.find({'usr_type': 'users'}))

# Find service
@APP.route('/services')
def get_services():
    """ Function to list services contained in the database """
    return render_template('pages/services.html',
                           services=MONGO.db.users.find(
                               {'usr_type': 'services'}))

# Find stores
@APP.route('/stores')
def get_stores():
    """ Function to list stores contained in the database """
    return render_template('pages/stores.html',
                           stores=MONGO.db.users.find({'usr_type': 'stores'}))

# UPDATE
@APP.route('/update/<usr_type>/<usr_id>', methods=['GET', 'POST'])
def update_entry(usr_type, usr_id):
    """
    Function to update entries on the database. It takes the user to determine
    the collection to be targeted and the user id to find the specific record
    in the collection.
    """

    if usr_type == 'dogs':
        user = MONGO.db.dogs
        get_user = 'get_dogs'

    else:
        get_user = 'get_'+str(usr_type)
        user = MONGO.db.users

    document = user.find_one()
    for key in document:
        if key != '_id':
            field_name = request.form.get(key)
            if field_name:
                user.update_one({'_id': ObjectId(usr_id)},
                                {'$set': {key: request.form.get(key)}})

    return redirect(url_for(get_user))


@APP.route('/feedback/<usr_type>/<receiver_id>', methods=['GET', 'POST'])
def user_feedback(usr_type, receiver_id):
    """
    Function to increment the number of feedbacks received by store or service,
    based on user inputs through the form.
    """
    user = MONGO.db.users
    if request.form.get('feedback-radio') == 'positive':
        user.update_one({'_id': ObjectId(receiver_id)},
                        {'$inc': {"fb_received.positive": 1}})
    if request.form.get('feedback-radio') == 'negative':
        user.update_one({'_id': ObjectId(receiver_id)},
                        {'$inc': {"fb_received.negative": 1}})

    if usr_type == 'services':
        url = 'get_services'
    else:
        url = 'get_stores'
    flash('Thanks for your feedback!', 'info')
    return redirect(url_for(url))


# DELETE
@APP.route('/delete/<usr_type>/<usr_id>', methods=['GET', 'POST'])
def delete_entry(usr_type, usr_id):
    if usr_type == 'dogs':
        usr = MONGO.db.dogs
        url = 'get_dogs'
    elif usr_type == 'not_adopted':
        usr = MONGO.db.adoptRequest
        url = 'get_adopt_requests'
    elif usr_type == 'adopted':
        usr = MONGO.db.adoptRequest
        adoption_file = usr.find_one({'_id': ObjectId(usr_id)})
        MONGO.db.dogs.delete_one({'_id': ObjectId(adoption_file['dog_id'])})
        url = 'get_adopt_requests'
    else:
        usr = MONGO.db.users
        url = 'get_'+str(usr_type)

    usr.delete_one({'_id': ObjectId(usr_id)})

    return redirect(url_for(url))


if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=False)
