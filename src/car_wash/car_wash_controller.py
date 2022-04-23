from . import car_wash_service
from flask import request, g
from src.role import role_middleware
from src.ticket import ticket_middleware
from src.auth import auth_middleware


# GET CAR WASH IDS
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin", "engineer", "owner"])
# @expiration_middleware.check_expiration(["owner"])
def get_car_wash_ids():
    res = car_wash_service.get_car_wash_ids_by_owner_id(owner_id=g.user_id) \
        if g.role_name == "owner" else \
        car_wash_service.get_car_wash_ids()
    return res


# GET CAR WASH IDS
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin", "engineer"])
def get_car_wash_ids_by_owner_id(owner_id: int):
    res = car_wash_service.get_car_wash_ids_by_owner_id(owner_id=owner_id)
    return res


# GET CAR WASH BY ID
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin", "engineer", "owner"])
# @expiration_middleware.check_expiration(["owner"])
def get_car_wash_by_id(car_wash_id: int):
    res = car_wash_service.get_car_wash_by_id_by_owner_id(car_wash_id=car_wash_id, owner_id=g.user_id) \
        if g.role_name == "owner" else \
        car_wash_service.get_car_wash_by_id(car_wash_id=car_wash_id)
    return res


# CREATE CAR WASH
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin", "engineer"])
def create_car_wash():
    req = request.get_json()
    res = car_wash_service.create_car_wash(
        title=req['title'],
        address=req['address'],
        owner_id=req['owner_id']
    )
    return res


# UPDATE CAR WASH
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin", "engineer"])
def update_car_wash(car_wash_id: int):
    req = request.get_json()
    res = car_wash_service.update_car_wash(car_wash_id=car_wash_id,
                                           title=req['title'],
                                           address=req['address'],
                                           owner_id=req['owner_id'])
    return res


# # CAR WASH LOGIN
# def car_wash_login() -> dict:
#     username: str = request.form.get('username')
#     password: str = request.form.get('password')
#     res: dict = car_wash_service.car_wash_login(username=username, password=password)
#     return res

