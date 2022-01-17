from src.services_db import role_service_db
from src._response import response


# GET ROLE IDS
def get_role_ids():
    ids = role_service_db.get_role_ids()
    return response(True, ids, 200)


# GET ROLE BY ID
def get_role_by_id(role_id):
    # GET ROLE BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    role = role_service_db.get_role_by_id(role_id=role_id)
    if not role:
        return response(False, {'msg': 'role not found'}, 404)

    # ELSE RETURN ROLE FIELDS
    return response(True, {'id': role.id, 'name': role.name}, 200)


# CREATE ROLE
def create_role(name):
    # GET ROLE BY NAME AND VERIFY. IF FOUND RETURN CONFLICT
    if role_service_db.get_role_by_name(name=name):
        return response(False, {'msg': 'role by this name exist'}, 409)

    # ELSE CREATE ROLE BY THIS NAME AND RETURN OK
    role = role_service_db.create_role(name=name)
    return response(True, {'msg': f'role by name {role.name} successfully created!'}, 201)


# UPDATE ROLE
def update_role(role_id, name):
    # GET ROLE BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not role_service_db.get_role_by_id(role_id=role_id):
        return response(False, {'msg': 'role not found'}, 404)

    # ELSE UPDATE ROLE AND RETURN OK
    role_service_db.update_role(role_id=role_id, name=name)
    return response(True, {'msg': 'role successfully updated!'}, 200)


# DELETE ROLE
def delete_role(role_id):
    # GET ROLE BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not role_service_db.get_role_by_id(role_id=role_id):
        return response(False, {'msg': 'role not found'}, 404)

    # ELSE DELETE ROLE BY THIS ID AND RETURN OK
    role_service_db.delete_role(role_id=role_id)
    return response(False, {'msg': 'role successfully deleted!'}, 200)
