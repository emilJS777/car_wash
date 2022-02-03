from functools import wraps
from src._response import response
from flask import request


# VALIDATE SCHEMA
def check_schema(schema):
    def decoration(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            body = request.get_json()
            print(body)
            return response(False, {'msg': 'forbidden'}, 403)
        return decorated_function
    return decoration
