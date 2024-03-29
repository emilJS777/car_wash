from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity
from src._response import response
from flask import request, g
from src.user import user_service_db
from . import auth_service_db
from .auth_service_db import Auth


# CHECk AUTHORIZE BY TOKEN
def check_authorize(f):
    @wraps(f)
    @jwt_required()
    def decorated_function(*args, **kwargs):
        # FIND USER AUTH FROM DB & CHECK IS A ACCESS_TOKEN. IF TOKENS MATCH, ASSIGN g.user_id user_id
        user_auth: Auth = auth_service_db.get_auth_by_user_id(user_id=get_jwt_identity())
        if user_auth.access_token == request.headers['authorization'].split(' ')[1]:

            # CHECK USER ON DB
            if user_service_db.get_user_by_id(user_id=get_jwt_identity()):
                g.user_id = get_jwt_identity()
                return f(*args, **kwargs)

        # IF THEY DON`T MATCH SEND A RESPONSE INVALID TOKEN UNAUTHORIZED
        return response(False, {'msg': 'invalid token'}, 401)

    return decorated_function
