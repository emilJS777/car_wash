from . import loyal_card_service, loyal_card_validator
from flask import request
from src.auth import auth_middleware
from src.role import role_middleware
from flask_expects_json import expects_json


# CREATE
@auth_middleware.check_authorize
@role_middleware.check_role(["owner"])
@expects_json(loyal_card_validator.bonus_card_schema)
def create() -> dict:
    req: dict = request.get_json()
    res: dict = loyal_card_service.create(
        code=req['code'],
        price=req['price'],
        full_name=req['full_name']
    )
    return res


# UPDATE
@auth_middleware.check_authorize
@role_middleware.check_role(["owner"])
@expects_json(loyal_card_validator.bonus_card_schema)
def update(bonus_card_id: int) -> dict:
    req: dict = request.get_json()
    res: dict = loyal_card_service.update(
        loyal_card_id=bonus_card_id,
        code=req['code'],
        price=req['price'],
        full_name=req['full_name']
    )
    return res


# DELETE
@auth_middleware.check_authorize
@role_middleware.check_role(["owner"])
def delete(loyal_card_id: int) -> dict:
    res: dict = loyal_card_service.delete(loyal_card_id)
    return res


# GET BY ID
@auth_middleware.check_authorize
@role_middleware.check_role(["owner", "client"])
def get_by_id(loyal_card_id: int) -> dict:
    res: dict = loyal_card_service.get_by_id(loyal_card_id)
    return res


# GET ALL IDS
@auth_middleware.check_authorize
@role_middleware.check_role(["owner", "client"])
def get_all_ids() -> dict:
    res: dict = loyal_card_service.get_all_ids()
    return res
