from src import db
from datetime import datetime


class Qr(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    img_path = db.Column(db.String(100), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())

    # CONSTRUCTOR
    def __init__(self, title, img_path):
        self.title = title
        self.img_path = img_path

    # SAVE DB SELF
    def save_db(self):
        db.session.add(self)
        db.session.commit()

    # DELETE DB
    def delete_db(self):
        db.session.delete(self)
        db.session.commit()

    # UPDATE DATABASE
    @staticmethod
    def update_db():
        db.session.commit()
