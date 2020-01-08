# Importing libraries
import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# from bs4 import BeautifulSoup

# Creating instance of Flask
app = Flask(__name__)
app.secret_key = 'SESSION_KEY'
# Adding Mongo database name and URI linking to that database.
# URI variable saved as environment variable on GitPod
app.config["MONGO_DBNAME"] = 'pawer'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

# Creating an instance of PyMongo
mongo = PyMongo(app)

@app.route('/')

@app.route('/user_home')
def user_home():
    """ Main page where users can choose where to go"""
    return render_template('user_home.html')

#Choosing type of account and adding a new user to database
@app.route('/register')
def register():
    """ Page where users can choose a type of account and register through the specific form"""
    return render_template('register.html')

#User Login
@app.route('/login', methods = ['GET','POST'])
def user_login():
    """ Loads page where users can login """
    users = mongo.db.users
    # services = mongo.db.services
    # stores = mongo.db.stores
    if request.method == 'POST':
        login_user = users.find_one({'_email' : request.form["login_email"]})
        # login_service = services.find_one({'_email' : request.form['_email']})
        # login_store = stores.find_one({'_email' : request.form['_email']})
        if login_user:
            if request.form['password'] == login_user['password']:
                session['username'] = login_user['_id']
                return redirect(url_for('user_home'))
        # if login_service:
        #     if request.form['password'] == login_service['password']
        #         session['username'] = login_service['_id']
        #         return redirect(url_for('user_home'))
        # if login_store:
        #     if request.form['password'] == login_store['password']
        #         session['username'] = login_store['_id']
        #         return redirect(url_for('user_home'))
    return render_template('login.html', user='invalid')

        



    return render_template('login.html')


#CREATE
#Add dog
@app.route('/new_dog', methods=['POST'])
def insert_dog():
    """ Function to add dogs to the database """
    #Check if the user already exists in the database
    if request.method == "POST":
        dogs = mongo.db.dogs
        existing_dog = dogs.find_one({'dog_name' : request.form['dog_name']})

        if existing_dog is None:
            dogs.insert_one(request.form.to_dict())
            return redirect(url_for('register'))
        
        return render_template('register.html', dog = True)

    return redirect(url_for('user_home'))

#Add user
@app.route('/new_user', methods=['POST'])
def insert_user():
    """ Function to add users to the database """
    users=mongo.db.users
    #Converting form to dictionary for Mongo
    users.insert_one(request.form.to_dict())
    #Redirecting user to home screen
    return redirect(url_for('user_home'))

#Add service
@app.route('/new_service', methods=['POST'])
def insert_service():
    """ Function to add services to the database """
    services=mongo.db.services
    #Converting form to dictionary for Mongo
    services.insert_one(request.form.to_dict())
    #Redirecting user to home screen
    return redirect(url_for('user_home'))

#Add store
@app.route('/new_store', methods=['POST'])
def insert_store():
    """ Function to add stores to the database """
    stores=mongo.db.stores
    #Converting form to dictionary for Mongo
    stores.insert_one(request.form.to_dict())
    #Redirecting user to home screen
    return redirect(url_for('user_home'))


#READ
#Find dog
@app.route('/dogs')
def get_dogs():
    """ Function to list dogs contained in the database """
    return render_template('dogs.html', dogs=mongo.db.dogs.find())

#Find user
@app.route('/users')
def get_users():
    """ Function to list users contained in the database """
    return render_template('users.html', users=mongo.db.users.find())

#Find service
@app.route('/services')
def get_services():
    """ Function to list services contained in the database """
    return render_template('services.html', services=mongo.db.services.find())

#Find stores
@app.route('/stores')
def get_stores():
    """ Function to list stores contained in the database """
    return render_template('stores.html', stores=mongo.db.stores.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)