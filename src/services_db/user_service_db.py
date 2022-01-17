from src.models.user_model import User


# # GET ALL USER IDS
# def get_all_ids():
#     ids = []
#     users = User.query.all()
#     for user in users:
#         ids.append(user.id)
#     return ids


# GET USER BY USER ID
def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user


# GET USER BY NAME AND RETURN
def get_user_by_name(name):
    user = User.query.filter_by(name=name).first()
    return user


# CREATE USER AND RETURN
def create_user(name, password, first_name, last_name):
    user = User(name=name, password=password, first_name=first_name, last_name=last_name)
    user.save_db()
    return user


# UPDATE USER AND RETURN
def update_user(user_id, name, first_name, last_name):
    user = User.query.filter_by(id=user_id).first()
    user.name = name
    user.first_name = first_name
    user.last_name = last_name
    user.update_db()
    return user


# DELETE USER AND RETURN
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    user.delete_db()
    return user
