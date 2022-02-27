from src import db
from datetime import datetime


class PaymentExpiration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payment_id = db.Column(db.String(150), unique=True, nullable=False)
    paid = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, nullable=False)
    payment_amount = db.Column(db.Numeric(8, 2), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())

    # CONSTRUCTOR
    def __init__(self, payment_id: str, user_id: int):
        self.payment_id = payment_id
        self.user_id = user_id

    # SAVE DB SELF
    def save_db(self):
        db.session.add(self)
        db.session.commit()

    # UPDATE DATABASE
    @staticmethod
    def update_db():
        db.session.commit()
