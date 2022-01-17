from src import db
from datetime import datetime


class DevicePayment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, nullable=False)
    payment = db.Column(db.Numeric(8, 2), nullable=False)
    currency = db.Column(db.String(4), nullable=False)
    topic = db.Column(db.String(120), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())

    # CONSTRUCTOR
    def __init__(self, device_id, payment, currency, topic):
        self.device_id = device_id
        self.payment = payment
        self.currency = currency
        self.topic = topic

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
