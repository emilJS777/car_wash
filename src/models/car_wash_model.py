from src import db


class CarWash(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)

    # CONSTRUCTOR
    def __init__(self, title, owner_id):
        self.title = title
        self.owner_id = owner_id

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
