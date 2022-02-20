from src.services_db import qr_service_db
from src.services_db.qr_service_db import Qr
from src._response import response
import qrcode
from datetime import datetime
import base64


# CREATE QR
def create_qr(title: str, url: str, img_path: str):
    # GET CURRENT QR AND VERIFY IF EXIST RETURN CONFLICT
    if qr_service_db.get_current_qr():
        return response(False, {'msg': 'qr code exist'}, 409)

    # GENERATE AND SAVE QR CODE
    new_qr_code = qrcode.QRCode(version=1, box_size=10, border=3)
    new_qr_code.add_data(url)
    new_qr_code.make(fit=True)
    image = new_qr_code.make_image(fill='black', back_color='white')
    image_path = img_path+str(datetime.now())+".png"
    image.save(image_path)

    # SAVE QR TITLE AND IMAGE PATH ON DB
    qr: Qr = qr_service_db.create_qr(title=title, img_path=image_path)
    return response(True, {'id': qr.id, 'title': qr.title, 'creation_date': qr.creation_date}, 200)


# GET CURRENT QR
def get_current_qr():
    # GET QR AND VERIFY IF NOT FOUND RETURN NOT FOUND
    qr: Qr = qr_service_db.get_current_qr()
    if not qr:
        return response(False, {'msg': 'qr not found'}, 404)

    # ELSE REtURN QR AND OK
    with open(qr.img_path, "rb") as binary_file:
        base64_encoded_data = base64.b64encode(binary_file.read())
        return response(True, {'id': qr.id, 'title': qr.title, 'img': str(base64_encoded_data.decode('utf-8')), 'creation_date': qr.creation_date}, 200)


# DELETE QR BY ID
def delete_qr_by_id(qr_id: int):
    # GET Qr BY ID AND VErIFY ID NoT FOUND REtuRN NOT FOUND
    if not qr_service_db.get_qr_by_id(qr_id=qr_id):
        return response(False, {'msg': "qr not found"}, 404)

    # ELSE DELETE QR BY ID
    qr_service_db.delete_qr(qr_id=qr_id)
    return response(True, {'msg': 'qr successfully deleted!'}, 200)
