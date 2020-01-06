# Importing libraries
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Creating instance of Flask
app = Flask(__name__)
# Adding Mongo database name and URI linking to that database.
# URI variable saved as environment variable on GitPod
app.config["MONGO_DBNAME"] = 'pawer'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

# Creating an instance of PyMongo
mongo = PyMongo(app)

@app.route('/')

@app.route('/user_home')
def user_home():
    return render_template('user_home.html')

#Reading 'dogs'
@app.route('/dogs')
def dogs_list():
    return render_template('dogs.html', dogs=mongo.db.dogs.find())


#Choosing type of account and adding a new user to database
@app.route('/register')
def register():
    return render_template('register.html', collections=mongo.db.list_collection_names())

#Add dog
@app.route('/new_dog', methods=['POST'])
def insert_dog():
    dogs = mongo.db.dogs
    #Converting form to dictionary for Mongo
    dogs.insert_one(request.form.to_dict())
    #Redirecting user to home screen
    return redirect(url_for('user_home'))

#Add user
@app.route('/new_user', methods=['POST'])
def insert_user():
    users=mongo.db.users
    #Converting form to dictionary for Mongo
    users.insert_one(request.form.to_dict())
    #Redirecting user to home screen
    return redirect(url_for('user_home'))

#Add service
@app.route('/new_service', methods=['POST'])
def insert_service():
    services=mongo.db.services
    #Converting form to dictionary for Mongo
    services.insert_one(request.form.to_dict())
    #Redirecting user to home screen
    return redirect(url_for('user_home'))

#Add store
@app.route('/new_store', methods=['POST'])
def insert_store():
    stores=mongo.db.stores
    #Converting form to dictionary for Mongo
    stores.insert_one(request.form.to_dict())
    #Redirecting user to home screen
    return redirect(url_for('user_home'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)