from flask import Flask, flash, render_template, redirect, request, url_for, session
# from flask_pymongo import PyMongo

from app import MONGO


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
    updates user entry to set "staff status" and "user type"
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


def get_user_by_email(form_email: str):
    """
    Queries the DB and returns user by email
    """
    users = MONGO.db.users
    return users.find_one({'email': form_email})


def get_dog_by_name(form_name: str):
    """
    Queries the DB and returns dog by name
    """
    dogs = MONGO.db.dogs
    return dogs.find_one({'dog_name': form_name['dog_name']})


def insert_user_or_dog(library: str, submitted_form: dict):
    """
    Inserts new user or dog to the database
    """
    library.insert_one(submitted_form.to_dict())


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


def get_existing_user_or_dog(usr_type: str, form: dict):
    """
    Queries database for existing user or dog
    """
    if usr_type == 'dogs':
        entry_exists = get_dog_by_name(form)
    else:
        entry_exists = get_user_by_email(form)

    if entry_exists:
        flash('Sorry, this entry already exists.', 'info')
        return redirect(url_for('add_entry'))
        
