from src.models.car_wash_model import CarWash


# GET CAR WASH IDS
def get_car_wash_ids():
    ids = []
    car_washes = CarWash.query.all()
    for car_wash in car_washes:
        ids.append(car_wash.id)
    return ids


# GET CAR WASH BY TITLE
def get_car_wash_by_title(title):
    car_wash = CarWash.query.filter_by(title=title).first()
    return car_wash


# GET CAR WASH BY ID
def get_car_wash_by_id(car_wash_id):
    car_wash = CarWash.query.filter_by(id=car_wash_id).first()
    return car_wash


# CREATE CAR WASH
def create_car_wash(title, owner_id):
    car_wash = CarWash(title=title, owner_id=owner_id)
    car_wash.save_db()
    return car_wash


# UPDATE CAR WASH
def update_car_wash(car_wash_id, title, owner_id):
    car_wash = CarWash.query.filter_by(id=car_wash_id).first()
    car_wash.title = title
    car_wash.owner_id = owner_id
    car_wash.update_db()
    return car_wash