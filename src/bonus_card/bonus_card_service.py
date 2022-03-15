from . import bonus_card_service_db
from src._response import response
from typing import List


# CREATE
def create(code: str, price: float) -> dict:
    # GET BY KEY IF EXIST RETURN CONFLICT
    if bonus_card_service_db.get_by_code(code):
        return response(False, {'msg': 'card by this key exist'}, 409)

    # ELSE CREATE NEW
    bonus_card_service_db.create(code, price)
    return response(True, {'msg': 'bonus card successfully created'}, 200)


# UPDATE
def update(bonus_card_id: int, code: str, price: float) -> dict:
    # GET BY ID IF NOT FOUND RETURN NOT FOUND
    if not bonus_card_service_db.get_by_id(bonus_card_id):
        return response(False, {'msg': 'bonus card not found'}, 404)

    # ELSE UPDATE
    bonus_card_service_db.update(
        bonus_card_id=bonus_card_id,
        code=code,
        price=price
    )
    return response(True, {'msg': 'bonus card successfully updated'}, 200)


# DELETE
def delete(bonus_card_id: int) -> dict:
    if not bonus_card_service_db.get_by_id(bonus_card_id):
        return response(False, {'msg': 'bonus card not found'}, 404)

    bonus_card_service_db.delete(bonus_card_id)
    return response(True, {'msg': 'bonus card successfully deleted'}, 200)


# GET BY ID
def get_by_id(bonus_card_id: int) -> dict:
    bonus_card: bonus_card_service_db.BonusCard = bonus_card_service_db.get_by_id(bonus_card_id)
    if not bonus_card:
        return response(False, {'msg': 'bonus card not found'}, 404)

    return response(True, {'id': bonus_card.id,
                           'key': bonus_card.code,
                           'price': bonus_card.price,
                           'owner_id': bonus_card.owner_id}, 200)


# GET ALL IDS
def get_all_ids() -> dict:
    bonus_card_ids: List[int] = bonus_card_service_db.get_all_ids()
    return response(True, bonus_card_ids, 200)
