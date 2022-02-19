from src.models.auth_model import Auth


# GENERATE TOKENS DB
def generate_pair_token(user_id) -> Auth:
    auth = Auth.query.filter_by(user_id=user_id).first() or Auth(user_id=user_id)
    auth.generate_access_token()
    auth.generate_refresh_token()
    auth.update_db() or auth.save_db()
    return auth


# GET AUTH BY USER ID
def get_auth_by_user_id(user_id) -> Auth:
    auth = Auth.query.filter_by(user_id=user_id).first()
    return auth
