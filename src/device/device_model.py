from src import db
from datetime import datetime


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(120), nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)
    water = db.Column(db.Boolean, default=False)
    lather = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=False)
    last_update = db.Column(db.DateTime, default=datetime.utcnow())

    # CONSTRUCTOR
    def __init__(self, code: str, owner_id: int):
        self.code = code,
        self.owner_id = owner_id

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
