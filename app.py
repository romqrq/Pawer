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
    # return 'Hello'

@app.route('/register')
def add_user():
    return render_template('register.html', collections=mongo.db.list_collection_names())

    



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)