# USER SCHEMA
create_user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 6},
        "first_name": {"type": "string", "minLength": 4},
        "last_name": {"type": "string", "minLength": 4},
        "password": {"type": "string", "minLength": 6}
      },
    "required": ["name", "first_name", "last_name", "password"]
}