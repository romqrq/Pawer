from flask import Flask, flash, render_template, session
from flask_pymongo import ObjectId
from app import MONGO


users = MONGO.db.users


def get_user_by_email(form_email: str):
    """
    Queries the DB and returns user by email
    """
    return users.find_one({'email': form_email})

def set_user_on_session(login_user: object):
    """
    Updates user id and user type(consumer, services, store) saved in the session.
    """
    session['user_id'] = str(login_user['_id'])
    session['user_type'] = login_user['usr_type']


def set_user_staff_status_on_session(login_user: object):
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
    -------------------
    Takes in the password and email from the submitted login form, checks if the email exists on the DB and
    compares the form and DB passwords
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