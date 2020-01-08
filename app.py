# Importing libraries
import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Creating instance of Flask
app = Flask(__name__)
#<=========================================
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
    
#CREATE
#Add dog
@app.route('/new_dog', methods=['POST'])
def insert_dog():
    """ Function to add dogs to the database """
    dogs = mongo.db.dogs
    #Converting form to dictionary for Mongo
    dogs.insert_one(request.form.to_dict())
    #Redirecting user to home screen
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