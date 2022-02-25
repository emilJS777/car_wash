# EMAIL SCHEMA
email_schema = {
    "type": "object",
    "properties": {
        "ticket_id": {"type": "number"},
        "address": {"type": "string", "minLength": 5,
                    "maxLength": 50,
                    "pattern": "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"}
      },
    "required": ["ticket_id", "address"]
}