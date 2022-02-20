from src.models.user_model import User


# # GET ALL USER IDS
# def get_all_ids():
#     ids = []
#     users = User.query.all()
#     for user in users:
#         ids.append(user.id)
#     return ids


# GET USER BY USER ID
def get_user_by_id(user_id: int) -> User:
    user: User = User.query.filter_by(id=user_id).first()
    return user


# GET USER BY NAME AND RETURN
def get_user_by_name(name: str) -> User:
    user: User = User.query.filter_by(name=name).first()
    return user


# CREATE USER AND RETURN
def create_user(name: str, password: str, first_name: str, last_name: str) -> User:
    user: User = User(name=name, password=password, first_name=first_name, last_name=last_name)
    user.save_db()
    return user


# UPDATE USER AND RETURN
def update_user(user_id: int, name: str, first_name: str, last_name: str) -> User:
    user: User = User.query.filter_by(id=user_id).first()
    user.name = name
    user.first_name = first_name
    user.last_name = last_name
    user.update_db()
    return user


# DELETE USER AND RETURN
def delete_user(user_id: int) -> User:
    user: User = User.query.filter_by(id=user_id).first()
    user.delete_db()
    return user
