from src.models.ticket_model import Ticket


# CREATE TICKET
def create_ticket(role_id):
    ticket = Ticket(code=Ticket.generate_ticket_code())
    ticket.role_id = role_id
    ticket.save_db()
    return ticket


# GET TICKET BY ROLE ID
def get_ticket_by_role_id(role_id):
    ticket = Ticket.query.filter_by(role_id=role_id).first()
    return ticket


# GET TICKET BY USER ID
def get_ticket_by_user_id(user_id):
    ticket = Ticket.query.filter_by(user_id=user_id).first()
    return ticket


# GET TICKET BY CODE
def get_ticket_by_code(code):
    ticket = Ticket.query.filter_by(code=code, active=False).first()
    return ticket


# UPDATE TICKET
def activate_ticket(ticket_id, user_id):
    ticket = Ticket.query.filter_by(id=ticket_id).first()
    ticket.code = "0"
    ticket.user_id = user_id
    ticket.active = True
    ticket.update_db()
    return ticket
