from flask import flash, redirect, url_for, render_template, session
# from app import user_home
import helper_functions.db_operations as db_op

from app import MONGO


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


def set_user_login(login_form: dict):
    """
    check_user_on_login
    -
    Function to check and control user login.
    
    Takes in the password and email from the submitted login form, checks if the email exists on the DB and
    compares the form and DB passwords and sets session variables
    """
    print('------------------')
    print(login_form)
    try:
        login_user = db_op.get_user_by_email(login_form['login_email'])

        if login_form['password'] == login_user['password']:

            set_user_on_session(login_user)

            set_user_staff_status_on_session(login_user)

            return True
        else:
            return False

    except Exception as e:
        print(e)
        # Expand on error handling