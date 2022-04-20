from src import db
from datetime import datetime


class LoyalCardPayment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loyal_card_id = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(8, 2), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())

    # CONSTRUCTOR
    def __init__(self, loyal_card_id: int, price: float):
        self.loyal_card_id = loyal_card_id
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
