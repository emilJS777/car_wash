from . import loyal_card_payment_service_db
from src.loyal_card import loyal_card_service_db
from src._response import response
from typing import List


def create_payment(loyal_card_code: str, price: float) -> dict:
    loyal_card: loyal_card_payment_service_db.LoyalCardPayment = loyal_card_service_db.get_by_code(
        loyal_card_code
    )

    if not loyal_card:
        return response(False, {'msg': 'loyal card not found'}, 404)

    if loyal_card.price < price:
        return response(False, {'msg': 'insufficient funds'}, 404)

    loyal_card_service_db.update(
        loyal_card_id=loyal_card.id,
        code=loyal_card.code,
        price=float(loyal_card.price) - float(price),
        full_name=loyal_card.full_name
    )

    loyal_card_payment_service_db.create_loyal_card_payment(
        loyal_card_id=loyal_card.id,
        price=price
    )
    return response(True, {'msg': 'payment successfully created'}, 200)


def delete_payment(loyal_card_payment_id: int) -> dict:
    if not loyal_card_payment_service_db.get_by_id(loyal_card_payment_id):
        return response(False, {'msg': 'loyal card not found'}, 404)

    loyal_card_payment_service_db.delete_loyal_card_payment(
        loyal_card_payment_id
    )
    return response(True, {'msg': 'payment successfully deleted'}, 200)


def get_payment_by_id(loyal_card_payment_id: int) -> dict:
    loyal_card_payment = loyal_card_payment_service_db.get_by_id(
        loyal_card_payment_id
    )
    if not loyal_card_payment:
        return response(False, {'msg': 'loyal card not found'}, 404)

    return response(True, {'id': loyal_card_payment.id,
                           'loyal_card_id': loyal_card_payment.loyal_card_id,
                           'price': loyal_card_payment.price,
                           'creation_date': loyal_card_payment.creation_date}, 200)


def get_all_ids_by_loyal_card_id(loyal_card_id: int) -> dict:
    if not loyal_card_service_db.get_by_id(loyal_card_id):
        return response(False, {'msg': 'bonus card not found'}, 404)

    loyal_card_ids: List[int] = loyal_card_payment_service_db.get_all_ids_by_loyal_card_id(
        loyal_card_id=loyal_card_id
    )
    return response(True, loyal_card_ids, 200)

