from src import db
from datetime import datetime


class BonusCardPayment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bonus_card_id = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(8, 2), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())

    # CONSTRUCTOR
    def __init__(self, bonus_card_id: int, price: float):
        self.bonus_card_id = bonus_card_id
        self.price = price

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
