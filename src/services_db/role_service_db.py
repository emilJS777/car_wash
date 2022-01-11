from src.models.role_model import Role


# CREATE ROLE
def create_role(title):
    role = Role(title=title)
    role.save_db()
    return role


# GET ROLE IDS
def get_role_ids():
    role_ids = []
    for role in Role.query.all():
        role_ids.append(role.id)
    return role_ids


# GET ROLE BY ID
def get_role_by_id(role_id):
    role = Role.query.filter_by(id=role_id).first()
    return role


# GET BY TITLE
def get_role_by_title(title):
    role = Role.query.filter_by(title=title).first()
    return role
