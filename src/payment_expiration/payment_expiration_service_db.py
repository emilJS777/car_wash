from .payment_expiration_model import PaymentExpiration
from flask import g


# CREATE PAYMENT EXPIRATION
def create_payment_expiration(payment_id: str) -> PaymentExpiration:
    payment_expiration = PaymentExpiration(payment_id=payment_id, user_id=g.user_id)
    payment_expiration.save_db()
    return payment_expiration
