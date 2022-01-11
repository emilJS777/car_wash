from src.models.user_model import User


# CREATE USER
def create_user(name, password):
    user = User(name=name, password=password)
    user.save_db()
    return user


# GET USER BY ID
def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user


# GET USER BY NAME
def get_user_by_name(name):
    user = User.query.filter_by(name=name).first()
    return user
