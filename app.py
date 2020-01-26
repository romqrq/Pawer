# Importing libraries
import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists('env.py'):
    import env
# from bs4 import BeautifulSoup

# Creating instance of Flask
app = Flask(__name__)
# app.secret_key = 'SESSION_KEY'
app.secret_key = os.environ.get('SECRET_KEY')
# SECRET_KEY = os.environ.get('SECRET_KEY')
# Adding Mongo database name and URI linking to that database.
# URI variable saved as environment variable on GitPod
app.config["MONGO_DBNAME"] = 'pawer'
# MONGO_URI = os.environ.get('MONGO_URI')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI', 'mongodb://localhost')

# Creating an instance of PyMongo
mongo = PyMongo(app)
@app.route('/')
# @app.route('/user_home')
def user_home():
    """ Main page where users can choose where to go"""
    return render_template('user_home.html')

# Choosing type of account and adding a new user to database
@app.route('/register')
def register():
    """ Page where users can choose a type of account and register through the specific form"""
    return render_template('register.html')

# User Login
@app.route('/login', methods=['GET', 'POST'])
def user_login():
    """ Loads page where users can login """
    users = mongo.db.users
    services = mongo.db.services
    stores = mongo.db.stores
    if request.method == 'POST':
        user_type = request.form["user_type_radio"]
        form_pwd = request.form['password']
        if user_type == 'user':
            login_user = users.find_one({'_email' : request.form['login_email']})
            if login_user:
                user_id = str(login_user['_id'])
                db_pwd = login_user['password']
                if form_pwd == db_pwd:
                    session['user_id'] = user_id
                    if login_user['is_staff']:
                        session['is_staff'] = login_user['is_staff']
                    else:
                        session['not_staff'] = 'not_staff'
                    return render_template('login.html', user='valid')
        if user_type == 'service':
            login_user = services.find_one({'_email': request.form['login_email']})
            if login_user:
                db_pwd = login_user['password']
                if form_pwd == db_pwd:
                    session['user_id'] = str(login_user['_id'])
                    return render_template('login.html', user='valid')
        if user_type == 'store':
            login_user = stores.find_one({'_email': request.form['login_email']})
            if login_user:
                db_pwd = login_user['password']
                if form_pwd == db_pwd:
                    session['user_id'] = str(login_user['_id'])
                    return render_template('login.html', user='valid')

        else: 
            return render_template('login.html', user='invalid')
 
    return render_template('login.html')

#USER LOGOUT
@app.route('/logout', methods=['GET', 'POST'])
def user_logout():
    """ Loads page where users can login """
    users = mongo.db.users
    services = mongo.db.services
    stores = mongo.db.stores
    if request.method == 'POST':
        user_type = request.form["user_type_radio"]
        form_pwd = request.form['password']
        if user_type == 'user':
            login_user = users.find_one({'_email' : request.form['login_email']})
            if login_user:
                user_id = str(login_user['_id'])
                db_pwd = login_user['password']
                if form_pwd == db_pwd:
                    session['user_id'] = user_id
                    # staff_user = login_user['is_staff']
                    if login_user['is_staff']:
                        session['is_staff'] = login_user['is_staff']
                    else:
                        session['not_staff'] = 'not_staff'
                    return render_template('login.html', user='valid')
        if user_type == 'service':
            login_user = services.find_one({'_email': request.form['login_email']})
            if login_user:
                db_pwd = login_user['password']
                if form_pwd == db_pwd:
                    return render_template('login.html', user='valid')
        if user_type == 'store':
            login_user = stores.find_one({'_email': request.form['login_email']})
            if login_user:
                db_pwd = login_user['password']
                if form_pwd == db_pwd:
                    return render_template('login.html', user='valid')

        else: 
            return render_template('login.html', user='invalid')
 
    return render_template('login.html')



# CREATE
#Add entry
@app.route('/new-entry/<usr_type>', methods=['POST'])
def add_entry(usr_type):
    existing_dog = None
    if usr_type == 'dogs':
        user = mongo.db.dogs
        existing_dog = user.find_one({'dog_name': request.form['dog_name']})
    elif usr_type == 'users':
        user = mongo.db.users
        existing_user = user.find_one({'_email': request.form['_email']})
    elif usr_type == 'services':
        user = mongo.db.services
        existing_user = user.find_one({'_email': request.form['_email']})
    else:
        user = mongo.db.stores
        existing_user = user.find_one({'_email': request.form['_email']})

    if request.method == 'POST':
        
        if existing_dog or existing_user:
            return render_template('register.html', existing_user=True)
        else:
            user.insert_one(request.form.to_dict())
            try:
                request.form['is_staff']
            except:
                user.update_one({'_email': request.form.get('_email')},
                        {'$set': {'is_staff': 'not_staff'} })
            return redirect(url_for('user_home'))
    


# Add dog
# @app.route('/new_dog', methods=['POST'])
# def insert_dog():
#     """ Function to add dogs to the database """
#     # Check if the user already exists in the database
#     if request.method == "POST":
#         dogs = mongo.db.dogs
#         existing_dog = dogs.find_one({'dog_name': request.form['dog_name']})

#         if existing_dog is None:
#             dogs.insert_one(request.form.to_dict())
#             return redirect(url_for('register'))
        
#         return render_template('register.html', existing_dog=True)

#     return redirect(url_for('user_home'))

# # Add user
# @app.route('/new_user', methods=['POST'])
# def insert_user():
#     """ Function to add users to the database """
#     users = mongo.db.users
#     # Check for existing user email. If the user exists, user gets visual feedback
#     existing_user = users.find_one({'_email': request.form['_email']})

#     if existing_user is None:
#         # If the user doesn't exists, convert form to dictionary and add to Mongo DB
#         users.insert_one(request.form.to_dict())
#         #Checking for 'is_staff' key, if none is returned from form, add key and value to user document on database.
#         try:
#             request.form['is_staff']
#         except:
#             users.update_one({'_email': request.form.get('_email')},
#                     {'$set': {'is_staff': 'not_staff'} })

#         return redirect(url_for('user_home'))
        
#     return render_template('register.html', existing_user=True)
    
    

# # Add service
# @app.route('/new_service', methods=['POST'])
# def insert_service():
#     """ Function to add services to the database """
#     services = mongo.db.services
#     # Converting form to dictionary for Mongo
#     services.insert_one(request.form.to_dict())
#     # Redirecting user to home screen
#     return redirect(url_for('user_home'))

# # Add store
# @app.route('/new_store', methods=['POST'])
# def insert_store():
#     """ Function to add stores to the database """
#     stores=mongo.db.stores
#     # Converting form to dictionary for Mongo
#     stores.insert_one(request.form.to_dict())
#     # Redirecting user to home screen
#     return redirect(url_for('user_home'))


# READ
# Find dog
@app.route('/dogs', methods=['GET', 'POST'])
def get_dogs():
    """ Function to list dogs contained in the database """
    return render_template('dogs.html', dogs=mongo.db.dogs.find())

# Find user
@app.route('/users')
def get_users():
    """ Function to list users contained in the database """
    return render_template('users.html', users=mongo.db.users.find())

# Find service
@app.route('/services')
def get_services():
    """ Function to list services contained in the database """
    return render_template('services.html', services=mongo.db.services.find())

# Find stores
@app.route('/stores')
def get_stores():
    """ Function to list stores contained in the database """
    return render_template('stores.html', stores=mongo.db.stores.find())

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
    elif usr_type == 'users':
        usr = mongo.db.users
        url = 'get_users'
    elif usr_type == 'services':
        usr = mongo.db.services
        url = 'get_services'
    else:
        usr = mongo.db.stores
        url = 'get_stores'
    usr.delete_one({'_id': ObjectId(usr_id)})
    return redirect(url_for(url))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)           