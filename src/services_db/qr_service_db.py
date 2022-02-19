from src.models.qr_model import Qr


# CREATE QR
def create_qr(title, img_path) -> Qr:
    qr = Qr(title=title, img_path=img_path)
    qr.save_db()
    return qr


# DELETE QR
def delete_qr(qr_id) -> Qr:
    qr = Qr.query.filter_by(id=qr_id).first()
    qr.delete_db()
    return qr


# GET QR BY ID
def get_qr_by_id(qr_id) -> Qr:
    qr = Qr.query.filter_by(id=qr_id).first()
    return qr


# GET CURRENT QR
def get_current_qr() -> Qr:
    qr = Qr.query.order_by(Qr.creation_date).first()
    return qr
