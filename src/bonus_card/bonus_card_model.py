from src import db


class BonusCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(120), unique=True, nullable=False)
    price = db.Column(db.Numeric, default=0)
    owner_id = db.Column(db.Integer, nullable=False)

    # CONSTRUCTOR
    def __init__(self, owner_id: int, code: str, price: float):
        self.code = code
        self.price = price
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
