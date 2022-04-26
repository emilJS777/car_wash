from src import db
from datetime import datetime


# DAILY COUNTER
class DeviceCounterDaily(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, unique=True, nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)

    coin = db.Column(db.Numeric(8, 2))
    bill = db.Column(db.Numeric(8, 2))
    cashless = db.Column(db.Numeric(8, 2))
    bonus = db.Column(db.Numeric(8, 2))
    service = db.Column(db.Numeric(8, 2))

    last_update = db.Column(db.DateTime, default=datetime.utcnow())

    # CONSTRUCTOR
    def __init__(self, device_id: int, owner_id: int):
        self.device_id = device_id
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


# TOTAL COUNTER
class DeviceCounterTotal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, unique=True, nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)

    coin = db.Column(db.Numeric(8, 2))
    bill = db.Column(db.Numeric(8, 2))
    cashless = db.Column(db.Numeric(8, 2))
    bonus = db.Column(db.Numeric(8, 2))
    service = db.Column(db.Numeric(8, 2))

    last_update = db.Column(db.DateTime, default=datetime.utcnow())

    # CONSTRUCTOR
    def __init__(self, device_id: int, owner_id: int):
        self.device_id = device_id
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
