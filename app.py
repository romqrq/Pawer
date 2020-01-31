# Importing libraries
import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists('env.py'):
    import env

# Creating instance of Flask
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
# Adding Mongo database name and URI linking to that database.
# URI variable saved as environment variable on GitPod
app.config["MONGO_DBNAME"] = 'pawer'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI', 'mongodb://localhost')

# Creating an instance of PyMongo
mongo = PyMongo(app)
@app.route('/')
def user_home():
    """ Main page where users can choose where to go"""
    return render_template('index.html')

# Choosing type of account and adding a new user to database
@app.route('/register')
def register():
    """ Page where users can choose a type of account and register through the specific form"""
    return render_template('register.html')

# User Login
@app.route('/login', methods=['GET', 'POST'])
def user_login():
    """ Loads page where users can login, checks the email and password on the database. If the user is valid, variables are added to session to be used 
        to adjust the content to the type of user and privileges """
    users = mongo.db.users
    if request.method == 'POST':
        form_pwd = request.form['password']
        login_user = users.find_one({'_email' : request.form['login_email']})
        if login_user:
            user_id = str(login_user['_id'])
            db_pwd = login_user['password']
            if form_pwd == db_pwd:
                session['user_id'] = user_id
                session['user_type'] = login_user['usr_type']
                if login_user['is_staff']:
                    session['is_staff'] = login_user['is_staff']
                else:
                    session['is_staff'] = 'not_staff'
                return render_template('index.html')
        else: 
            return render_template('login.html', user='invalid')
 
    return render_template('login.html')

#USER LOGOUT
@app.route('/logout', methods=['GET', 'POST'])
def user_logout():
    """ Simplified logout function that removes items added to the session list during login """

    session.pop('user_id')
    session.pop('is_staff')
    session.pop('user_type')

    return render_template('index.html')

#DASHBOARD
@app.route('/dashboard', methods=['GET', 'POST'])
def get_dashboard():
    """ Function to load the dashboard where users can update their account details or delete their account."""
    usr_id = session['user_id']
    return render_template('dashboard/dashboard.html', user=mongo.db.users.find_one({'_id': ObjectId(usr_id)}))
    
# CREATE
#Add entry
@app.route('/new-entry/<usr_type>', methods=['POST'])
def add_entry(usr_type):
    """ Function to create new document in the users collection. It looks up for pre-existing records and only adding to database if the record doesn't exist.
        The function also adds the 'staff' status of the account and the account type."""
    existing_dog = None
    if usr_type == 'dogs':
        user = mongo.db.dogs
        existing_dog = user.find_one({'dog_name': request.form['dog_name']})
    else:
        user = mongo.db.users
        existing_user = user.find_one({'_email': request.form['_email']})

    if existing_user:
        return render_template('register.html', existing_user=True)
    elif existing_dog:
        return render_template('register.html', existing_dog=True)
    else:
        user.insert_one(request.form.to_dict())
        try:
            request.form['is_staff']
        except:
            user.update_one({'_email': request.form.get('_email')},
                    {'$set': {'is_staff': 'not_staff',
                                'usr_type': usr_type} })
        
        return redirect(url_for('user_home'))

#Adopt a dog
@app.route('/adopt/<usr_id>/<dog_id>', methods=['GET', 'POST'])
def adopt_dog(usr_id, dog_id):
    """ Function to create new document in the adoptRequest collection. It gets information from the adoptant and the dog to create a single file."""
    adopt = mongo.db.adoptRequest
    this_user = mongo.db.users.find_one({'_id': ObjectId(usr_id)})
    adopt.insert_one(this_user)
    
    for key in this_user:
        if key == '_id':
            adopt.update_one({'_email': this_user['_email']},
                            {'$set': {'usr_id': this_user[key]} })


    this_dog = mongo.db.dogs.find_one({'_id': ObjectId(dog_id)})
    for key in this_dog:
        if key == '_id':
            adopt.update_one({'_email': this_user['_email']},
                            {'$set': {'dog_id': this_dog[key]} })
        if key != '_id':
            adopt.update_one({'_email': this_user['_email']},
                            {'$set': {key: this_dog[key]} })

    return redirect(url_for('get_dogs'))

# READ
#List adoption requests
@app.route('/requests', methods=['GET', 'POST'])
def get_adopt_requests():
    return render_template('requests.html', requests=mongo.db.adoptRequest.find())

# Find dog
@app.route('/dogs', methods=['GET', 'POST'])
def get_dogs():
    """ Function to list dogs contained in the database """
    return render_template('dogs.html', dogs=mongo.db.dogs.find())

# Find user
@app.route('/users')
def get_users():
    """ Function to list users contained in the database """
    return render_template('users.html', users=mongo.db.users.find({'usr_type': 'users'}))

# Find service
@app.route('/services')
def get_services():
    """ Function to list services contained in the database """
    return render_template('services.html', services=mongo.db.users.find({'usr_type': 'services'}))

# Find stores
@app.route('/stores')
def get_stores():
    """ Function to list stores contained in the database """
    return render_template('stores.html', stores=mongo.db.users.find({'usr_type': 'stores'}))

# UPDATE
@app.route('/update/<usr_type>/<usr_id>', methods=['GET', 'POST'])
def update_entry(usr_type, usr_id):

    if usr_type == 'dogs':
        user = mongo.db.dogs
        get_user = 'get_dogs'
    elif usr_type == 'users':
        user = mongo.db.users
        get_user = 'get_users'
    elif usr_type == 'services':
        user = mongo.db.services
        get_user = 'get_services'
    else:
        user = mongo.db.stores
        get_user = 'get_stores'
    
    document = user.find_one()
    for key in document:
        if key != '_id':
            field_name = request.form.get(key)
            if field_name:
                user.update_one({'_id': ObjectId(usr_id)},
                    {'$set': {key: request.form.get(key)} })
    
    return redirect(url_for(get_user))

# DELETE
@app.route('/delete/<usr_type>/<usr_id>', methods=['GET', 'POST'])
def delete_entry(usr_type, usr_id):
    if usr_type == 'dogs':
        usr = mongo.db.dogs
        url = 'get_dogs'
    elif usr_type == 'not_adopted':
        usr = mongo.db.adoptRequest
        url = 'get_adopt_requests'
    elif usr_type == 'adopted':
        usr = mongo.db.adoptRequest
        adoption_file = usr.find_one({'_id': ObjectId(usr_id)})
        print('--------------------------------')
        print(usr_id)
        print(adoption_file['dog_id'])
        mongo.db.dogs.delete_one({'_id': ObjectId(adoption_file['dog_id'])})
        url = 'get_adopt_requests'
    else:
        usr = mongo.db.users
        url = 'get_users'

     
    usr.delete_one({'_id': ObjectId(usr_id)})

    return redirect(url_for(url))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)           