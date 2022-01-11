from src.services import role_service
from src.middlewares import auth_middleware, role_middleware


# GET ROLE BY ID
@auth_middleware.check_authorize
@role_middleware.check_roles(["engineer"])
def get_role_by_id(role_id):
    res = role_service.get_role_by_id(role_id=role_id)
    return res


# GET ROLE IDS
@auth_middleware.check_authorize
@role_middleware.check_roles(["engineer"])
def get_role_ids():
    res = role_service.get_role_ids()
    return res
