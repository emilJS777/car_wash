from src import db
from flask_bcrypt import generate_password_hash
# from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    # role_id = db.Column(db.Integer, nullable=False)
    # registration_code = db.Column(db.String(50), unique=True, nullable=True)
    # active = db.Column(db.Boolean, default=True)
    # expiration_date = db.Column(db.DateTime, default=datetime.utcnow())

    # CONSTRUCTOR
    def __init__(self, name: str, password: str, first_name: str, last_name: str):
        self.name = name
        self.password_hash = generate_password_hash(password)
        self.first_name = first_name
        self.last_name = last_name

    # SAVE DB SELF
    def save_db(self):
        db.session.add(self)
        db.session.commit()

    # UPDATE DATABASE
    @staticmethod
    def update_db():
        db.session.commit()
