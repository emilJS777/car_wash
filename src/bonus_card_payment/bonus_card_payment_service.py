from . import bonus_card_payment_service_db
from src.bonus_card import bonus_card_service_db
from src._response import response
from typing import List


def create_payment(bonus_card_code: str, price: float) -> dict:
    bonus_card: bonus_card_payment_service_db.BonusCardPayment = bonus_card_service_db.get_by_code(
        bonus_card_code
    )

    if not bonus_card:
        return response(False, {'msg': 'bonus card not found'}, 404)

    if bonus_card.price < price:
        return response(False, {'msg': 'insufficient funds'}, 404)

    bonus_card_service_db.update(
        bonus_card_id=bonus_card.id,
        code=bonus_card.code,
        price=float(bonus_card.price) - float(price)
    )

    bonus_card_payment_service_db.create_bonus_card_payment(
        bonus_card_id=bonus_card.id,
        price=price
    )
    return response(True, {'msg': 'payment successfully created'}, 200)


def delete_payment(bonus_card_payment_id: int) -> dict:
    if not bonus_card_payment_service_db.get_by_id(bonus_card_payment_id):
        return response(False, {'msg': 'bonus card not found'}, 404)

    bonus_card_payment_service_db.delete_bonus_card_payment(
        bonus_card_payment_id
    )
    return response(True, {'msg': 'payment successfully deleted'}, 200)


def get_payment_by_id(bonus_card_payment_id: int) -> dict:
    bonus_card_payment = bonus_card_payment_service_db.get_by_id(
        bonus_card_payment_id
    )
    if not bonus_card_payment:
        return response(False, {'msg': 'bonus card not found'}, 404)

    return response(True, {'id': bonus_card_payment.id,
                           'bonus_card_id': bonus_card_payment.bonus_card_id,
                           'price': bonus_card_payment.price,
                           'creation_date': bonus_card_payment.creation_date}, 200)


def get_all_ids_by_bonus_card_id(bonus_card_id: int) -> dict:
    if not bonus_card_service_db.get_by_id(bonus_card_id):
        return response(False, {'msg': 'bonus card not found'}, 404)

    bonus_card_ids: List[int] = bonus_card_payment_service_db.get_all_ids_by_bonus_card_id(
        bonus_card_id=bonus_card_id
    )
    return response(True, bonus_card_ids, 200)

