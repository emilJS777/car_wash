from src.services_db import email_service_db, ticket_service_db
from src._response import response


# GET EMAIL BY TICKET ID
def get_email_by_ticket_id(ticket_id):
    # GET EMAIL BY TICKET ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    email = email_service_db.get_email_by_ticket_id(ticket_id=ticket_id)
    if not email:
        return response(False, {'msg': 'email not found'}, 404)

    # ELSE RETURN EMAIL FIELDS AND OK
    return response(True, {'id': email.id, 'address': email.address}, 200)


# CREATE EMAIL
def create_email(ticket_id, address):
    # GET TICKET BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not ticket_service_db.get_ticket_by_id(ticket_id=ticket_id):
        return response(False, {'msg': 'ticket not found'}, 404)

    # GET EMAIL BY ADDRESS AND VERIFY. IF EXIST RETURN CONFLICT
    if email_service_db.get_email_by_address(address=address):
        return response(False, {'msg': 'email by this address exist'}, 409)

    # ELSE CREATE EMAIL AND RETURN OK
    email = email_service_db.create_email(ticket_id=ticket_id, address=address)
    return response(True, {'id': email.id, 'address': email.address}, 200)


# SEND TICKET CODE BY EMAIL ID
def send_ticket_code_by_email_id(email_id):
    # GET EMAIL BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    email = email_service_db.get_email_by_id(email_id=email_id)
    if not email:
        return response(False, {'msg': 'email not found'}, 404)

    # GET TICKET FROM EMAIL TICKET ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    ticket = ticket_service_db.get_ticket_by_id(ticket_id=email.ticket_id)
    if not ticket:
        return response(False, {'msg': 'ticket not found'}, 404)

    # ELSE SEND BY EMAIL TICKET ACTIVATION CODE AND RETURN OK
    email_service_db.send_ticket_code_by_email_id(email_id=email.id, ticket_code=ticket.code)
    return response(True, {'msg': f'by address {email.address} ticket code {ticket.code} sent successfully'}, 200)
