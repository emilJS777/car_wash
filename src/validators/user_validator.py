# USER CREATE SCHEMA
create_user_schema = {
    "type": "object",
    "properties": {
        "email": { "type": "string", "minLength": 6, "pattern": "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$" },
        "name": { "type": "string", "minLength": 6},
        "password": {"type": "string", "minLength": 6},
        "passwordConfirm":  {"type": "string", "minLength": 6}
      },
    "required": ["email", "name", "password"]
}