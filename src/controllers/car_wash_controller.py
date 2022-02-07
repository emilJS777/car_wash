from src.services import car_wash_service
from flask import request, g
from src.middlewares import auth_middleware, role_middleware, ticket_middleware


# GET CAR WASH IDS
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin", "engineer", "owner"])
def get_car_wash_ids():
    res = car_wash_service.get_car_wash_ids()
    return res


# GET CAR WASH BY ID
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin", "engineer", "owner"])
def get_car_wash_by_id(car_wash_id):
    res = car_wash_service.get_car_wash_by_id(car_wash_id=car_wash_id)
    return res


# CREATE CAR WASH
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["engineer"])
def create_car_wash():
    req = request.get_json()
    res = car_wash_service.create_car_wash(title=req['title'], address=req['address'], owner_id=req['owner_id'])
    return res


# UPDATE CAR WASH
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["engineer"])
def update_car_wash(car_wash_id):
    req = request.get_json()
    res = car_wash_service.update_car_wash(car_wash_id=car_wash_id, title=req['title'],
                                           address=req['address'], owner_id=req['owner_id'])
    return res

