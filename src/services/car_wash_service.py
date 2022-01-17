from src.services_db import car_wash_service_db, user_service_db
from src._response import response


# GET CAR WASH IDS
def get_car_wash_ids():
    car_wash_ids = car_wash_service_db.get_car_wash_ids()
    return response(True, car_wash_ids, 200)


# GET CAR WASH BY ID
def get_car_wash_by_id(car_wash_id):
    # GET CAR WASH BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    car_wash = car_wash_service_db.get_car_wash_by_id(car_wash_id=car_wash_id)
    if not car_wash:
        return response(False, {'msg': 'car wash not found'}, 404)

    # ELSE RETURN CAR WASH FIELDS AND OK
    return response(True, {'id': car_wash.id, 'title': car_wash.title, 'owner_id': car_wash.owner_id}, 200)


# CREATE CAR WASH
def create_car_wash(title, owner_id):
    # GET CAR WASH BY TITLE AND VERIFY. IF EXIST RETURN CONFLICT
    if car_wash_service_db.get_car_wash_by_title(title=title):
        return response(False, {'msg': 'car wash by this title exist'}, 409)

    # GET USER BY OWNER ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not user_service_db.get_user_by_id(user_id=owner_id):
        return response(False, {'msg': 'owner not found'}, 404)

    # ELSE CREATE NEW CAR WASH AND RETURN OK
    car_wash = car_wash_service_db.create_car_wash(title=title, owner_id=owner_id)
    return response(True, {'msg': f'car wash by title {car_wash.title} successfully created!'}, 201)


# UPDATE CAR WASH
def update_car_wash(car_wash_id, title, owner_id):
    # GET CAR WASH BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not car_wash_service_db.get_car_wash_by_id(car_wash_id=car_wash_id):
        return response(False, {'msg': 'car wash not found'}, 404)

    # GET USER BY OWNER ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not user_service_db.get_user_by_id(user_id=owner_id):
        return response(False, {'msg': 'owner not found'}, 404)

    # ELSE UPDATE CAR WASH AND RETURN OK
    car_wash = car_wash_service_db.update_car_wash(car_wash_id=car_wash_id, title=title, owner_id=owner_id)
    return response(True, {'msg': f'car wash by id {car_wash.id} successfully updated!'}, 200)
