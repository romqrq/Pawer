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
    return render_template('user_home.html', dogs=mongo.db.dogs.find())

#Choosing what type of account
@app.route('/choose_account')
def choose_account():
    return render_template('choose_account.html', collections=mongo.db.list_collection_names())

#Creating a new user and adding to database
@app.route('/add_user')
def add_user():
    return render_template('add_user.html')

@app.route('/insert_user', methods=['POST'])
def insert_user():
    users=mongo.db.users
    #Converting form to dictionary for Mongo
    users.insert_one(request.form.to_dict())
    #Redirecting user to home screen
    return redirect(url_for('user_home'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)