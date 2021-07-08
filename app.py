# Importing libraries
import os
from os import path
from re import DEBUG
from dns.rdatatype import NULL
from flask import Flask, flash, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if path.exists('env.py'):
    import env

DEBUG = True

# Creating instance of Flask
APP = Flask(__name__)
APP.secret_key = os.environ.get('SECRET_KEY')

# Adding Mongo database name and URI linking to that database.
APP.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
APP.config["MONGO_URI"] = os.environ.get('MONGO_URI')

# Creating an instance of PyMongo
MONGO = PyMongo(APP)

# Importing helper functions
from helper_functions import data_manipulation as data_mnpt, db_operations as db_op, entry_checks as check_entry, session_manipulation as session_mnpt



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
        login_check = session_mnpt.set_user_login(request.form.to_dict())
        if login_check: 
            flash('Welcome Back! You were successfully logged in.', 'info')
            return redirect(url_for('user_home'))
        else:
            flash('Invalid email or password.', 'info')
            return redirect(url_for('user_login'))
    else:
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
    if request.form:
        entry_exists = check_entry.check_existing_user_or_dog(usr_type, request.form)

        if entry_exists:
            flash('Sorry, this entry already exists.')
            return redirect(url_for('register'))

    if usr_type == 'dogs':
        db_op.create_dog(request.form.to_dict())

    else:
        db_op.create_user(request.form.to_dict())

        if usr_type == 'services' or usr_type == 'stores':
            db_op.update_feedback_key_to_user(request.form.to_dict())

        db_op.update_staff_status_and_user_type_on_user(usr_type, request.form.to_dict())
    
    flash('You have been successfully registered! Welcome!', 'info')
    return redirect(url_for('user_home'))

# Adopt a dog
@APP.route('/adopt/<usr_id>/<dog_id>', methods=['GET', 'POST'])
def adopt_dog(usr_id, dog_id):
    """ Function to create new entry in the adoptRequest collection.
    It gets information from the adoptant and the dog to create a single
    file."""

    existing_request = check_entry.check_existing_adoption_request(usr_id)
    if existing_request:
        flash('We already have one request from you. We will get in touch very soon!', 'info')
        return redirect(url_for('get_dogs'))

    adopt_req = data_mnpt.build_adoption_request(usr_id, dog_id, request.form.to_dict())
    
    db_op.create_adoption_request(adopt_req)

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
                           services=MONGO.db.users.find({'usr_type': 'services'}))

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
    target_url = data_mnpt.build_target_url(usr_type)

    entry_exists = check_entry.check_existing_user_or_dog(usr_type, usr_id, request.form.to_dict())
    if entry_exists:
        prepd_data = data_mnpt.set_missing_submitted_form_fields(usr_type, usr_id, request.form.to_dict())
        db_op.update_user_or_dog_through_form(prepd_data[0], prepd_data[1], prepd_data[2])
    else:
        flash('Sorry, there seems to be a problem with this database entry.', 'info')
        return redirect(url_for(target_url))

    flash('Done! Entry successfully updated.', 'info')
    return redirect(url_for(target_url))


@APP.route('/feedback/<usr_type>/<receiver_id>', methods=['GET', 'POST'])
def user_feedback(usr_type, receiver_id):
    """
    Function to increment the number of feedbacks received by store or service,
    based on user inputs through the form.
    """

    db_op.update_user_feedback(receiver_id, feedback_form = request.form.to_dict())

    target_url = data_mnpt.build_target_url(usr_type)

    flash('Thanks for your feedback!', 'info')
    return redirect(url_for(target_url))


# DELETE
@APP.route('/delete/<usr_type>/<usr_id>', methods=['GET', 'POST'])
def delete_entry(usr_type, usr_id):
    """
    Function to delete database entries. It deletes the entry depending on the user type.
    """
    if usr_type == 'dogs':
        db_op.delete_dog(usr_id)

    elif usr_type == 'not_adopted':
        db_op.delete_adoption_request(usr_id)

    elif usr_type == 'adopted':
        adoption_request = db_op.get_adoption_request(usr_id)
        db_op.delete_dog(adoption_request['dog_id'])
        db_op.delete_adoption_request(usr_id)

    else:
        db_op.delete_user(usr_id)

    target_url = data_mnpt.build_target_url(usr_type)

    flash('This entry has been deleted.', 'info')
    return redirect(url_for(target_url))


if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=False)
