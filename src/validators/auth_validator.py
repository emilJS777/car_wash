# LOGIN SCHEMA
login_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 1},
        "password": {"type": "string", "minLength": 1}
      },
    "required": ["name", "password"]
}