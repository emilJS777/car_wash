from src.services import qr_service
from src import app
from flask import request
from src.middlewares import auth_middleware, role_middleware


# GET CURRENT Qr
@auth_middleware.check_authorize
@role_middleware.check_role(["admin", "owner"])
def get_current_qr():
    res = qr_service.get_current_qr()
    return res


# CREATE QR
@auth_middleware.check_authorize
@role_middleware.check_role(["admin"])
def create_qr():
    req = request.get_json()
    res = qr_service.create_qr(title=req["title"], url=req["url"], img_path=app.config["QR_IMG_PATH"])
    return res


# DELETE QR BY ID
@auth_middleware.check_authorize
@role_middleware.check_role(["admin"])
def delete_qr(qr_id):
    res = qr_service.delete_qr_by_id(qr_id=qr_id)
    return res
