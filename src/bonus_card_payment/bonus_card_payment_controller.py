from . import bonus_card_payment_service
from flask import request
from src.auth import auth_middleware
from src.role import role_middleware


def create_payment() -> dict:
    req = request.args
    res: dict = bonus_card_payment_service.create_payment(
        bonus_card_code=req['bonus_card_code'],
        price=float(req['price'])
    )
    return res


@auth_middleware.check_authorize
@role_middleware.check_role(["owner"])
def delete_payment(bonus_card_payment_id: int) -> dict:
    res: dict = bonus_card_payment_service.delete_payment(bonus_card_payment_id)
    return res


@auth_middleware.check_authorize
@role_middleware.check_role(["owner"])
def get_payment_by_id(bonus_card_payment_id: int) -> dict:
    res: dict = bonus_card_payment_service.get_payment_by_id(bonus_card_payment_id)
    return res


@auth_middleware.check_authorize
@role_middleware.check_role(["owner"])
def get_all_ids_by_bonus_card_id(bonus_card_id: int) -> dict:
    res: dict = bonus_card_payment_service.get_all_ids_by_bonus_card_id(bonus_card_id)
    return res



