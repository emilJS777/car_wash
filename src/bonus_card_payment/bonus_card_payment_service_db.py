from .bonus_card_payment_model import BonusCardPayment
from typing import List


# CREATE
def create_bonus_card_payment(bonus_card_id: int, price: float) -> BonusCardPayment:
    bonus_card_payment: BonusCardPayment = BonusCardPayment(
        bonus_card_id=bonus_card_id,
        price=price
    )
    bonus_card_payment.save_db()
    return bonus_card_payment


# DELETE
def delete_bonus_card_payment(bonus_card_payment_id: int) -> BonusCardPayment:
    bonus_card_payment: BonusCardPayment = BonusCardPayment.query.filter_by(id=bonus_card_payment_id).first()
    bonus_card_payment.delete_db()
    return bonus_card_payment


# GET BY ID
def get_by_id(bonus_card_payment_id: int) -> BonusCardPayment:
    bonus_card_payment: BonusCardPayment = BonusCardPayment.query.filter_by(id=bonus_card_payment_id).first()
    return bonus_card_payment


# GET ALL IDs BY BONUS CARD ID
def get_all_ids_by_bonus_card_id(bonus_card_id: int) -> List[int]:
    bonus_card_payments: List[BonusCardPayment] = BonusCardPayment.query.filter_by(bonus_card_id=bonus_card_id).all()
    bonus_card_payment_ids: List[int] = []

    for bonus_card_payment in bonus_card_payments:
        bonus_card_payment_ids.append(bonus_card_payment.id)

    return bonus_card_payment_ids

