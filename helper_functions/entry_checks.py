from app import MONGO
import helper_functions.db_operations as db_op


def check_existing_user_or_dog(usr_type: str, entry_id: str, form: dict):
    """
    Queries database for existing user or dog
    """
    if usr_type == 'dogs':
        entry_exists = db_op.get_dog_by_id(entry_id)
    else:
        entry_exists = db_op.get_user_by_id(entry_id)
    return entry_exists


def check_existing_adoption_request(usr_id: str):
    """
    Queries database for existing adoption request
    """
    existing_request = db_op.get_adoption_request(usr_id)
    
    return existing_request