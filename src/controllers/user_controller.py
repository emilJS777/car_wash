from src.services import user_service
from flask import request
from flask_expects_json import expects_json
from src.validators import user_validator


@expects_json(user_validator.create_user_schema)
def create_user():
    req = request.get_json()
    res = user_service.create_user(name=req['name'], password=req['password'],
                                   email=req['email'], ticket_code=req['ticket_code'])
    return res
