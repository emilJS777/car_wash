from src.services import car_wash_service
from flask import request
from src.middlewares import auth_middleware, role_middleware


# GET CAR WASH IDS
@auth_middleware.check_authorize
@role_middleware.check_role(["admin", "engineer"])
def get_car_wash_ids():
    res = car_wash_service.get_car_wash_ids()
    return res


# GET CAR WASH BY ID
@auth_middleware.check_authorize
@role_middleware.check_role(["admin", "engineer"])
def get_car_wash_by_id(car_wash_id):
    res = car_wash_service.get_car_wash_by_id(car_wash_id=car_wash_id)
    return res


# CREATE CAR WASH
@auth_middleware.check_authorize
@role_middleware.check_role(["engineer"])
def create_car_wash():
    req = request.get_json()
    res = car_wash_service.create_car_wash(title=req['title'], owner_id=req['owner_id'])
    return res


# UPDATE CAR WASH
@auth_middleware.check_authorize
@role_middleware.check_role(["engineer"])
def update_car_wash(car_wash_id):
    req = request.get_json()
    res = car_wash_service.update_car_wash(car_wash_id=car_wash_id, title=req['title'], owner_id=req['owner_id'])
    return res

