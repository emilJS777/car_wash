from src.services import ticket_service
from src.middlewares import auth_middleware, role_middleware, ticket_middleware


# GET ENGINEER TICKETS
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin"])
def get_engineer_tickets():
    res = ticket_service.get_tickets_by_role_name(role_name=["engineer"])
    return res


# GET OWNER TICKETS
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin", "engineer"])
def get_owner_tickets():
    res = ticket_service.get_tickets_by_role_name(role_name=["owner"])
    return res


# CREATE TICKET
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(['admin', 'engineer'])
def create_ticket():
    res = ticket_service.create_ticket()
    return res


# DELETE TICKET
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(['admin', 'engineer'])
def delete_ticket(ticket_id):
    res = ticket_service.delete_ticket(ticket_id=ticket_id)
    return res


# ACTIVATE OR DEACTIVATE TICKET BY ID
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(['admin', 'engineer'])
def activate_or_deactivate_ticket(ticket_id):
    res = ticket_service.activate_or_deactivate_ticket(ticket_id=ticket_id)
    return res

