from flask import request, g
from flask_jwt_extended import get_jwt_identity
from src.services_db import auth_service_db, user_service_db
from src._response import response
from flask_bcrypt import check_password_hash
from src.services_db import ticket_service_db, role_service_db, user_service_db


# LOGIN
def login(name, password):
    # GET USER BY NAME AND CHECK EXIST OR PASSWORD
    user = user_service_db.get_user_by_name(name=name)
    if not user or not check_password_hash(user.password_hash, password):
        return response(False, {'msg': 'user not found'}, 404)

    # GENERATE PAIR TOKEN
    auth = auth_service_db.generate_pair_token(user_id=user.id)
    return response(True, {'access_token': auth.access_token, 'refresh_token': auth.refresh_token}, 200)


# REFRESH
def refresh():
    # GET AUTH BY USER ID AND CHECK FOR COMPLIANCE WITH THE REFRESH TOKEN
    auth = auth_service_db.get_auth_by_user_id(user_id=get_jwt_identity())
    if auth.refresh_token == request.headers['authorization'].split(' ')[1]:

        # UPON MATCHING, A NEW PAIR OF TOKENS IS GENERATED AND RESPOND
        new_auth = auth_service_db.generate_pair_token(user_id=get_jwt_identity())
        return response(True, {'access_token': new_auth.access_token, 'refresh_token': new_auth.refresh_token}, 200)

    # IF DO NOT MATCH RETURN WITHOUT SUCCESS
    else:
        return response(False, {'msg': 'invalid refresh token'}, 401)


# GET PROFILE BY AUTH
def get_profile():
    # GET TICKET, USER, ROLE BY G.USER_ID AND RETURN FIELDS AND OK
    ticket = ticket_service_db.get_ticket_by_user_id(user_id=g.user_id)
    user = user_service_db.get_user_by_id(user_id=g.user_id)
    role = role_service_db.get_role_by_id(role_id=ticket.role_id)
    return response(True, {'first_name': user.first_name, 'last_name': user.last_name,
                           'user_name': user.name, 'role_name': role.name}, 200)
