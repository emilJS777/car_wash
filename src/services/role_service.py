from src.services_db import role_service_db
from src._response import response


# GET ROLE BY ID
def get_role_by_id(role_id):
    # GET ROLE AND VERIFY EXIST OR NOT . IF NO RETURN 404
    role = role_service_db.get_role_by_id(role_id=role_id)
    if not role:
        return response(False, {'msg': f'role by id {role_id} not found'}, 404)

    # ELSE RETURN ROLE ID AND TITLE
    return response(True, {'id': role.id, 'title': role.title}, 200)


# GET ROLE IDS
def get_role_ids():
    role_ids = role_service_db.get_role_ids()
    return response(True, role_ids, 200)
