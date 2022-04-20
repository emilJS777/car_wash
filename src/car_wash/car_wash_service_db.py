from .car_wash_model import CarWash
from typing import List


# GET CAR WASH IDS
def get_car_wash_ids() -> List[int]:
    ids: List[int] = []
    car_washes: List[CarWash] = CarWash.query.all()
    for car_wash in car_washes:
        ids.append(car_wash.id)
    return ids


# GET CAR WASH IDS BY OWNER ID
def get_car_wash_ids_by_owner_id(owner_id: int) -> List[int]:
    ids: List[int] = []
    car_washes: List[CarWash] = CarWash.query.filter_by(owner_id=owner_id).all()
    for car_wash in car_washes:
        ids.append(car_wash.id)
    return ids


# GET CAR WASH BY TITLE
def get_car_wash_by_title(title: str) -> CarWash:
    car_wash: CarWash = CarWash.query.filter_by(title=title).first()
    return car_wash


# GET CAR WASH BY ID
def get_car_wash_by_id(car_wash_id: int) -> CarWash:
    car_wash: CarWash = CarWash.query.filter_by(id=car_wash_id).first()
    return car_wash


# GET CAR WASH BY ID BY OWNER ID
def get_car_wash_by_id_by_owner_id(car_wash_id: int, owner_id: int) -> CarWash:
    car_wash: CarWash = CarWash.query.filter_by(id=car_wash_id, owner_id=owner_id).first()
    return car_wash


# GET CAR WASH BY USERNAME
def get_car_wash_by_username(username: str) -> CarWash:
    car_wash: CarWash = CarWash.query.filter_by(username=username).first()
    return car_wash


# CREATE CAR WASH
def create_car_wash(title: str, address: str, owner_id: int, username: str, password: str) -> CarWash:
    car_wash: CarWash = CarWash(
        title=title,
        address=address,
        owner_id=owner_id,
        username=username,
        password=password
    )
    car_wash.save_db()
    return car_wash


# UPDATE CAR WASH
def update_car_wash(car_wash_id: int, title: str, address: str, owner_id: int) -> CarWash:
    car_wash: CarWash = CarWash.query.filter_by(id=car_wash_id).first()
    car_wash.title = title
    car_wash.address = address
    car_wash.owner_id = owner_id
    car_wash.update_db()
    return car_wash
