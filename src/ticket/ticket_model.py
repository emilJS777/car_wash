from src import db
from datetime import datetime


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=True)
    code = db.Column(db.String(50), unique=True, nullable=True)
    active = db.Column(db.Boolean, default=True)
    expiration_date = db.Column(db.DateTime, default=datetime.utcnow())

    # CONSTRUCTOR
    def __init__(self, role_id: int):
        self.role_id = role_id

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
