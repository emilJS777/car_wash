from src.services_db import user_service_db, ticket_service_db, role_service_db
from src._response import response


# GET USER BY ID
def get_user_by_id(user_id):
    # GET USER BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    user = user_service_db.get_user_by_id(user_id=user_id)
    if not user:
        return response(False, {'msg': 'user by this id not found'}, 404)

    # ELSE GET USER BY THIS ID AND RETURN USER FIELDS
    return response(True, {"id": user.id, "name": user.name, "first_name": user.first_name,
                           "last_name": user.last_name}, 200)


# CREATE USER
def create_user(name, first_name, last_name, password, ticket_code=None):
    # GET AND VERIFY. EXIST USER BY THIS NAME, IF YES RETURN CONFLICTs
    if user_service_db.get_user_by_name(name=name):
        return response(False, {'msg': 'user by this username exist'}, 409)

    # CREATE TICKET OR GET EXIST TICKET AND UPDATE - ASSIGN USER ID FIELD
    if ticket_code:
        ticket = ticket_service_db.get_ticket_by_code(code=ticket_code)

        # IF TICKET NOT FOUND RETURN NOT FOUND
        if not ticket:
            return response(False, {'msg': 'ticket code not found'}, 404)
    # ELSE IF NOT TICKET CODE CREATE NEW TICKET FOR CLIENT USER
    else:
        ticket = ticket_service_db.create_ticket(role_id=role_service_db.get_role_by_name(name="client").id)

    # ELSE CREATE USER
    user = user_service_db.create_user(name=name, first_name=first_name, last_name=last_name, password=password)

    # ASSIGN TICKET USER ID AND RETURN RESPONSE OK
    ticket_service_db.update_ticket(ticket_id=ticket.id, user_id=user.id)

    return response(True, {'msg': f'user by id {user.id} successfully created!'}, 201)


# UPDATE USER
def update_user(user_id, name, first_name, last_name):
    # GET USER BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not user_service_db.get_user_by_id(user_id=user_id):
        return response(False, {'msg': 'user by this id not found'}, 404)

    # ELSE UPDATE USER BY THIS ID AND RETURN OK
    user = user_service_db.update_user(user_id=user_id, name=name, first_name=first_name, last_name=last_name)
    return response(True, {'msg': f'user by id {user.id} successfully updated'}, 200)


# DELETE USER
def delete_user(user_id):
    # GET USER BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not user_service_db.get_user_by_id(user_id=user_id):
        return response(False, {'msg': 'user by this id not found'}, 404)

    # ELSE DELETE USER BY THIS ID AND RETURN OK
    user = user_service_db.delete_user(user_id=user_id)
    return response(True, {'msg': f'user by id {user.id} successfully deleted!'}, 200)
