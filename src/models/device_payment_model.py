from src import db
from datetime import datetime


class DevicePayment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(8, 2), nullable=False)
    currency = db.Column(db.String(4), nullable=False)
    type = db.Column(db.String(120), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())

    # CONSTRUCTOR
    def __init__(self, device_id, price, currency, type, owner_id):
        self.device_id = device_id
        self.owner_id = owner_id
        self.price = price
        self.currency = currency
        self.type = type

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
