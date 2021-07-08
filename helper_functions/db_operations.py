import os
from flask import request
from bson.objectid import ObjectId

from app import MONGO

# from helper_functions import data_manipulation as data_mnpt

users = MONGO.db.users
dogs = MONGO.db.dogs
adopt = MONGO.db.adoptRequest

def get_user_by_email(user_email: str):
    """
    Queries the DB and returns user by email
    """
    return users.find_one({'email': user_email})


def get_user_by_id(user_id: str):
    """
    Queries the DB and returns user by id
    """
    return users.find_one({'_id': ObjectId(user_id)})


def get_dog_by_name(dog_name: str):
    """
    Queries the DB and returns dog by name
    """
    return dogs.find_one({'dog_name': dog_name})


def get_dog_by_id(dog_id: str):
    """
    Queries the DB and returns dog by id
    """
    return dogs.find_one({'_id': ObjectId(dog_id)})


def get_adoption_request(adoption_request_id: str):
    """
    Queries the DB and returns dog by id
    """
    existing_request = adopt.find_one({'usr_id': ObjectId(adoption_request_id)})

    return existing_request


def create_user(submitted_form: dict):
    """
    Creates new user to the database
    """
    users.insert_one(submitted_form)


def create_dog(submitted_form: dict):
    """
    Creates new dog to the database
    """
    dogs.insert_one(submitted_form)


def create_adoption_request(adoption_request: dict):
    """
    Creates new adoption request entry to the database
    """
    adopt.insert_one(adoption_request)


def update_feedback_key_to_user(form):
    """
    updates entry to add "feedback" key with initial values to stores and service user types.
    """
    users.update_one({'email': request.form['email']},
                     {'$set': {'fb_received': {'positive': 0,
                                               'negative': 0}}})


def update_staff_status_and_user_type_on_user(usr_type: str, form: dict):
    """
    Updates user entry to set "staff status" and "user type"
    """
    users.update_one({'email': form['email']},
                    {'$set': {'is_staff': form['is_staff'],
                                'usr_type': usr_type}})


def update_user_or_dog_through_form(library: str, target: dict, modified_form: dict):
    """
    Updates user or dog entry using submitted form
    """
    for key in target:
        if key != '_id':
            field_name = modified_form[key]
            if field_name:
                library.update_one({'_id': target['_id']},
                                    {'$set': {key: modified_form[key]}})


def update_user_feedback(receiver_id: str, feedback_form: dict):
    """
    Increments in 1 the number of feedbacks received by the user depending on it being
    positive or negative
    """
    if feedback_form['feedback-radio'] == 'positive':
        users.update_one({'_id': ObjectId(receiver_id)},
                         {'$inc': {"fb_received.positive": 1}})
    if feedback_form['feedback-radio'] == 'negative':
        users.update_one({'_id': ObjectId(receiver_id)},
                         {'$inc': {"fb_received.negative": 1}})


def delete_adoption_request(adoption_request_id: str):
    """
    Deletes adoption request entry from database.
    """
    adopt.delete_one({'_id': ObjectId(adoption_request_id)})


def delete_dog(dog_id:str):
    """
    Deletes dog entry from database.
    """
    dogs.delete_one({'_id': ObjectId(dog_id)})


def delete_user(user_id:str):
    """
    Deletes user entry from database.
    """
    users.delete_one({'_id': ObjectId(user_id)})