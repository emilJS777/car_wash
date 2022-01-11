from src.models.email_model import Email


# CREATE EMAIL
def create_email(address, user_id):
    email = Email(address=address, user_id=user_id)
    email.save_db()
    return email


# GET EMAIL USER ID
def get_email_by_user_id(user_id):
    email = Email.query.filter_by(user_id=user_id).first()
    return email

