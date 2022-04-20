from .loyal_card_payment_model import LoyalCardPayment
from typing import List


# CREATE
def create_loyal_card_payment(loyal_card_id: int, price: float) -> LoyalCardPayment:
    loyal_card_payment: LoyalCardPayment = LoyalCardPayment(
        loyal_card_id=loyal_card_id,
        price=price
    )
    loyal_card_payment.save_db()
    return loyal_card_payment


# DELETE
def delete_loyal_card_payment(loyal_card_payment_id: int) -> LoyalCardPayment:
    loyal_card_payment: LoyalCardPayment = LoyalCardPayment.query.filter_by(id=loyal_card_payment_id).first()
    loyal_card_payment.delete_db()
    return loyal_card_payment


# GET BY ID
def get_by_id(loyal_card_payment_id: int) -> LoyalCardPayment:
    loyal_card_payment: LoyalCardPayment = LoyalCardPayment.query.filter_by(id=loyal_card_payment_id).first()
    return loyal_card_payment


# GET ALL IDs BY LOYAL CARD ID
def get_all_ids_by_loyal_card_id(loyal_card_id: int) -> List[int]:
    loyal_card_payments: List[LoyalCardPayment] = LoyalCardPayment.query.filter_by(loyal_card_id=loyal_card_id).all()
    loyal_card_payment_ids: List[int] = []

    for loyal_card_payment in loyal_card_payments:
        loyal_card_payment_ids.append(loyal_card_payment.id)

    return loyal_card_payment_ids

