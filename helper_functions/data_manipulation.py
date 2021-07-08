import helper_functions.db_operations as db_op
from app import MONGO


def build_adoption_request(user_id: str, dog_id: str, submitted_form: dict):
    """
    Builds new adoption request dictionary to match required parameters for database entry
    """
    this_user = db_op.get_user_by_id(user_id)
    this_dog = db_op.get_dog_by_id(dog_id)

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
    elif user_type == 'not_adopted' or user_type == 'adopted':
        target_url = 'get_adopt_requests'
    else:
        target_url = 'get_'+str(user_type)

    return target_url


def set_missing_submitted_form_fields(usr_type: str, entry_id: str, submitted_form: dict):
    """
    Prepares data for entry updates: sets target, sets library values and adds possibly
    missing fields on submitted forms.
    """
    if usr_type == 'dogs':
        target = db_op.get_dog_by_id(entry_id)
        library = MONGO.db.dogs
    else:
        target = db_op.get_user_by_id(entry_id)
        library = MONGO.db.users
    
    for key in target:

        if key != '_id' and key not in submitted_form:
            submitted_form[key] = ''

    return library, target, submitted_form



