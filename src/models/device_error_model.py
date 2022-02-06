from src import db
from datetime import datetime


class DeviceError(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_code = db.Column(db.Integer, nullable=False)
    msg = db.Column(db.String(300), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())

    # CONSTRUCTOR
    def __init__(self, device_code, msg):
        self.device_code = device_code,
        self.msg = msg

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
