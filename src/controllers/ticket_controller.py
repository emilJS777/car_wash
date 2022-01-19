from src.services import ticket_service
from src.middlewares import auth_middleware, role_middleware


# CREATE TICKET
@auth_middleware.check_authorize
@role_middleware.check_role(['admin', 'engineer'])
def create_ticket():
    res = ticket_service.create_ticket()
    return res


# DELETE TICKET
@auth_middleware.check_authorize
@role_middleware.check_role(['admin', 'engineer'])
def delete_ticket(ticket_id):
    res = ticket_service.delete_ticket(ticket_id=ticket_id)
    return res
