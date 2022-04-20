from src import db
from datetime import datetime


class CarWash(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=False, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(180), nullable=False, unique=True)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())

    # CONSTRUCTOR
    def __init__(self, title: str, address: str, owner_id: int, username: str, password: str):
        self.title = title
        self.address = address
        self.owner_id = owner_id
        self.username = username
        self.password = password

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
