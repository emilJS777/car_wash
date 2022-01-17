from src.models.role_model import Role


# GET ROLE IDS
def get_role_ids():
    ids = []
    roles = Role.query.all()
    for role in roles:
        ids.append(role.id)
    return ids


# GET ROLE BY NAME
def get_role_by_name(name):
    role = Role.query.filter_by(name=name).first()
    return role


# GET ROLE BY ID
def get_role_by_id(role_id):
    role = Role.query.filter_by(id=role_id).first()
    return role


# CREATE ROLE
def create_role(name):
    role = Role(name=name)
    role.save_db()
    return role


# UPDATE ROLE
def update_role(role_id, name):
    role = Role.query.filter_by(id=role_id).first()
    role.name = name
    return role


# DELETE ROLE
def delete_role(role_id):
    role = Role.query.filter_by(id=role_id).first()
    role.delete_db()
    return role

