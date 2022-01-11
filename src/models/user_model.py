from src import db
from flask_bcrypt import generate_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(250), nullable=True)

    # CONSTRUCTOR
    def __init__(self, name, password):
        self.name = name
        self.password_hash = generate_password_hash(password)

    # SAVE DB SELF
    def save_db(self):
        db.session.add(self)
        db.session.commit()

    # DELETE DB
    def delete_db(self):
        db.session.delete(self)
        db.session.commit()

    # UPDATE DATABASE
    @staticmethod
    def update_db():
        db.session.commit()
