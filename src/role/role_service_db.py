from .role_model import Role
from typing import List


# GET ROLE IDS
def get_role_ids() -> List[int]:
    ids: List[int] = []
    roles: List[Role] = Role.query.all()
    for role in roles:
        ids.append(role.id)
    return ids


# GET ROLE BY NAME
def get_role_by_name(name: str) -> Role:
    role: Role = Role.query.filter_by(name=name).first()
    return role


# GET ROLE BY ID
def get_role_by_id(role_id: int) -> Role:
    role: Role = Role.query.filter_by(id=role_id).first()
    return role


# CREATE ROLE
def create_role(name: str) -> Role:
    role: Role = Role(name=name)
    role.save_db()
    return role


# UPDATE ROLE
def update_role(role_id: int, name: str) -> Role:
    role: Role = Role.query.filter_by(id=role_id).first()
    role.name = name
    return role


# DELETE ROLE
def delete_role(role_id) -> Role:
    role = Role.query.filter_by(id=role_id).first()
    role.delete_db()
    return role

