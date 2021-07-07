from flask import Flask, flash, render_template, redirect, request, url_for, session
from bson.objectid import ObjectId
# from flask_pymongo import PyMongo

from app import MONGO


def get_user_by_email(form_email: str):
    """
    Queries the DB and returns user by email
    """
    users = MONGO.db.users
    return users.find_one({'email': form_email})


def get_user_by_id(user_id: str):
    """
    Queries the DB and returns user by id
    """
    users = MONGO.db.users
    return users.find_one({'_id': user_id})


def get_dog_by_name(form_name: str):
    """
    Queries the DB and returns dog by name
    """
    dogs = MONGO.db.dogs
    return dogs.find_one({'dog_name': form_name['dog_name']})


def get_dog_by_id(dog_id: str):
    """
    Queries the DB and returns dog by id
    """
    dogs = MONGO.db.dogs
    return dogs.find_one({'_id': dog_id})


def get_existing_user_or_dog(usr_type: str, form: dict):
    """
    Queries database for existing user or dog
    """
    if usr_type == 'dogs':
        entry_exists = get_dog_by_name(form)
    else:
        entry_exists = get_user_by_email(form)
    
    return entry_exists


def get_existing_adoption_request(usr_id: str):
    """
    Queries database for existing adoption request
    """
    adopt = MONGO.db.adoptRequest
    existing_request = adopt.find_one({'usr_id': ObjectId(usr_id)})
    
    if existing_request:
        flash('We already have one request from you. We will get in touch very soon!', 'info')
        return redirect(url_for('get_dogs'))


def create_user_or_dog(library: str, submitted_form: dict):
    """
    Creates new user or dog to the database
    """
    library.insert_one(submitted_form.to_dict())


def create_adoption_request(adoption_request: dict):
    """
    Creates new adoption request entry to the database
    """
    adopt = MONGO.db.adoptRequest
    adopt.insert_one(adoption_request)


def build_adoption_request(user_id: str, dog_id: str, submitted_form: dict):
    """
    Builds new adoption request dictionary to match required parameters for database entry
    """
    this_user = this_user = MONGO.db.users.find_one({'_id': ObjectId(user_id)})
    this_dog = MONGO.db.dogs.find_one({'_id': ObjectId(dog_id)})

    adopt_req = {**this_user, **this_dog}

    adopt_req.update({'usr_id': this_user['_id'], 'dog_id': this_dog['_id'],
                      'why_adopt': submitted_form['why_adopt']})

    return adopt_req


def build_target_url(user_type: str):
    """
    Builds target url depending on the user type
    """
    if user_type == 'dogs':
        target_url = 'get_dogs'
    else:
        target_url = 'get_'+str(user_type)

    return target_url


def update_feedback_key_to_user(form):
    """
    updates entry to add "feedback" key with initial values to stores and service user types.
    """
    users = MONGO.db.users
    users.update_one({'email': request.form['email']},
                     {'$set': {'fb_received': {'positive': 0,
                                               'negative': 0}}})


def update_staff_status_and_user_type_on_user(usr_type: str, form: dict):
    """
    Updates user entry to set "staff status" and "user type"
    """
    try:
        request.form['is_staff']
        usr_type.update_one({'email': form['email']},
                        {'$set': {'is_staff': 'is_staff',
                                  'usr_type': usr_type}})
    except KeyError:
        usr_type.update_one({'email': form['email']},
                        {'$set': {'is_staff': 'not_staff',
                                  'usr_type': usr_type}})


# def update_dog_through_form(dog_id: str, submitted_form: dict):
#     """
#     Updates dog entry
#     """
#     dogs = MONGO.db.dogs
#     dog = get_dog_by_id(dog_id)
    
#     for key in dog:
#         if key != '_id':
#             field_name = submitted_form[key]
#             if field_name:
#                 dogs.update_one({'_id': ObjectId(dog_id)},
#                                 {'$set': {key: submitted_form[key]}})


def update_user_or_dog_through_form(usr_type: str, entry_id: str, submitted_form: dict):
    """
    Updates user or dog entry using submitted form
    """
    if usr_type == 'dogs':
        target = get_dog_by_name(submitted_form)
        library = MONGO.db.dogs
    else:
        target = get_user_by_email(submitted_form)
        library = MONGO.db.users

    for key in target:
        if key != '_id':
            field_name = submitted_form[key]
            if field_name:
                library.update_one({'_id': ObjectId(entry_id)},
                                    {'$set': {key: submitted_form[key]}})
    


# def update_user_through_form(user_id: str, submitted_form: dict):
#     """
#     Updates user entry
#     """
#     users = MONGO.db.users
#     user = get_user_by_id(user_id)
    
#     for key in user:
#         if key != '_id':
#             field_name = submitted_form[key]
#             if field_name:
#                 users.update_one({'_id': ObjectId(user_id)},
#                                 {'$set': {key: submitted_form[key]}})


def set_user_on_session(login_user: dict):
    """
    Updates user id and user type(consumer, services, store) saved in the session.
    """
    session['user_id'] = str(login_user['_id'])
    session['user_type'] = login_user['usr_type']


def set_user_staff_status_on_session(login_user: dict):
    """
    Updates user staff status in the session.
    """
    if login_user['is_staff']:
        session['is_staff'] = login_user['is_staff']
    else:
        session['is_staff'] = 'not_staff'
    

def check_user_on_login(form_pwd: str, form_email: str):
    """
    check_user_on_login
    -
    Function to check and control user login.
    
    Takes in the password and email from the submitted login form, checks if the email exists on the DB and
    compares the form and DB passwords and sets session variables
    """
    try:
        login_user = get_user_by_email(form_email)

        if form_pwd == login_user['password']:

            set_user_on_session(login_user)

            set_user_staff_status_on_session(login_user)

            flash('Welcome Back! You were successfully logged in.', 'info')
            return render_template('pages/index.html')
        else:
            flash('Invalid email or password.', 'info')

    except Exception as e:
        print(e)
        flash('Invalid email or password.', 'info')



        
