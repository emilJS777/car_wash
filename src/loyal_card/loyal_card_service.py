from . import loyal_card_service_db
from src._response import response
from typing import List


# CREATE
def create(code: str, price: float, full_name: str) -> dict:
    # GET BY KEY IF EXIST RETURN CONFLICT
    if loyal_card_service_db.get_by_code(code):
        return response(False, {'msg': 'card by this key exist'}, 409)

    # ELSE CREATE NEW
    loyal_card_service_db.create(
        code=code,
        price=price,
        full_name=full_name
    )
    return response(True, {'msg': 'bonus card successfully created'}, 200)


# UPDATE
def update(loyal_card_id: int, code: str, price: float, full_name: str) -> dict:
    # GET BY ID IF NOT FOUND RETURN NOT FOUND
    if not loyal_card_service_db.get_by_id(loyal_card_id):
        return response(False, {'msg': 'bonus card not found'}, 404)

    # ELSE UPDATE
    loyal_card_service_db.update(
        loyal_card_id=loyal_card_id,
        code=code,
        price=price,
        full_name=full_name
    )
    return response(True, {'msg': 'bonus card successfully updated'}, 200)


# DELETE
def delete(loyal_card_id: int) -> dict:
    if not loyal_card_service_db.get_by_id(loyal_card_id):
        return response(False, {'msg': 'bonus card not found'}, 404)

    loyal_card_service_db.delete(loyal_card_id)
    return response(True, {'msg': 'bonus card successfully deleted'}, 200)


# GET BY ID
def get_by_id(loyal_card_id: int) -> dict:
    loyal_card: loyal_card_service_db.LoyalCard = loyal_card_service_db.get_by_id(loyal_card_id)
    if not loyal_card:
        return response(False, {'msg': 'bonus card not found'}, 404)

    return response(True, {'id': loyal_card.id,
                           'code': loyal_card.code,
                           'price': loyal_card.price,
                           'owner_id': loyal_card.owner_id,
                           'full_name:': loyal_card.full_name}, 200)


# GET ALL IDS
def get_all_ids() -> dict:
    loyal_card_ids: List[int] = loyal_card_service_db.get_all_ids()
    return response(True, loyal_card_ids, 200)
