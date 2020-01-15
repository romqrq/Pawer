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
@app.route('/login', methods = ['GET', 'POST'])
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
                staff_user = str(login_user['is_staff'])
                db_pwd = login_user['password']
                if form_pwd == db_pwd:
                    session['user_id'] = user_id
                    if staff_user:
                        session['is_staff'] = staff_user
                    return render_template('login.html', user='valid')
        if user_type == 'service':
            login_user = services.find_one({'_email' : request.form['login_email']})
            if login_user:
                db_pwd = login_user['password']
                if form_pwd == db_pwd:
                    return render_template('login.html', user='valid')
        if user_type == 'store':
            login_user = stores.find_one({'_email' : request.form['login_email']})
            if login_user:
                db_pwd = login_user['password']
                if form_pwd == db_pwd:
                    return render_template('login.html', user='valid')

        else: return render_template('login.html', user='invalid')
 
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
@app.route('/dogs', methods=['GET','POST'])
def get_dogs():
    """ Function to list dogs contained in the database """
    # if request.method == 'POST':
    #     if request.form['value']=='dogs':
    #         usr_id = request.form['id']
    #         return update_dog(usr_id)

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

#UPDATE
@app.route('/dogs/<usr_id>', methods=['GET', 'POST'])
def update_dog(usr_id):
    dogs=mongo.db.dogs
    dogs.update({'_id' : ObjectId(usr_id)}, 
    {
        'dog_name':request.form.get('dog_name'),
        'dog_breed':request.form.get('dog_breed'),
        'dog_description':request.form.get('dog_description')
    })
    # return redirect(url_for('get_dogs', edit_dog=mongo.db.dogs.find_one({'_id': usr_id})))
    return redirect(url_for('get_dogs'))


@app.route('/user/<usr_id>', methods=['GET', 'POST'])
def update_user(usr_id):
    user=mongo.db.users
    user.update({'_id' : ObjectId(usr_id)},
    {
        'first_name':request.form.get('first_name'),
        'last_name':request.form.get('last_name'),
        'password':request.form.get('password'),
        '_email':request.form.get('_email'),
        'is_staff':request.form.get('is_staff'),
        'user_description':request.form.get('user_description')
    })
    return redirect(url_for('get_users'))


@app.route('/services/<usr_id>', methods=['GET', 'POST'])
def update_service(user_id):
    service=mongo.db.services
    service.update({'_id' : ObjectId(usr_id)}, 
    {
        'first_name':request.form.get('first_name'),
        'last_name':request.form.get('last_name'),
        'type_of_service':request.form.get('type_of_service'),
        'service_description':request.form.get('service_description'),
        '_email':request.form.get('_email'),
        'password':request.form.get('password')
    })
    return redirect(url_for('get_service'))

@app.route('/stores/<usr_id>', methods=['GET', 'POST'])
def update_store(usr_id):
    store=mongo.db.stores
    store.update({'_id' : ObjectId(usr_id)},
    {
        'store_name':request.form.get('store_name'),
        'store_address':request.form.get('store_address'),
        'store_description':request.form.get('store_description'),
        '_email':request.form.get('_email')
    })
    return redirect(url_for('get_stores'))

#DELETE
@app.route('/dogs/<usr_id>', methods=['GET', 'POST'])
def delete_dog(usr_id):
    mongo.db.dogs.deleteOne({'_id': ObjectId(usr_id)})
    return redirect(url_for('get_dogs'))

@app.route('/users/<usr_id>', methods=['GET', 'POST'])
def delete_user(usr_id):
    mongo.db.users.deleteOne({'_id': ObjectId(usr_id)})
    return redirect(url_for('get_users'))

@app.route('/service/<usr_id>', methods=['GET', 'POST'])
def delete_service(usr_id):
    mongo.db.services.deleteOne({'_id': ObjectId(usr_id)})
    return redirect(url_for('get_services'))

@app.route('/stores/<usr_id>', methods=['GET', 'POST'])
def delete_store(usr_id):
    mongo.db.stores.deleteOne({'_id': ObjectId(usr_id)})
    return redirect(url_for('get_stores'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)