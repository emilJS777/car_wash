from src import db


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(50), unique=True, nullable=False)

    # CONSTRUCTOR
    def __init__(self, ticket_id, address):
        self.ticket_id = ticket_id
        self.address = address

    # SAVE DB SELF
    def save_db(self):
        db.session.add(self)
        db.session.commit()

    # UPDATE DATABASE
    @staticmethod
    def update_db():
        db.session.commit()
