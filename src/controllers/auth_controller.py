from flask import request
from flask_jwt_extended import jwt_required
from src.services import auth_service
from flask_expects_json import expects_json
from src.validators import auth_validator
from src.middlewares import auth_middleware


@expects_json(auth_validator.login_schema)
def login():
    req = request.get_json()
    res = auth_service.login(name=req['name'], password=req['password'])
    return res


@jwt_required(refresh=True)
def refresh():
    res = auth_service.refresh()
    return res

