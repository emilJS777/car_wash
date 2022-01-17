from src.services import ticket_service
from src.middlewares import auth_middleware, role_middleware


# CREATE TICKET
@auth_middleware.check_authorize
@role_middleware.check_role(['admin', 'engineer'])
def create_ticket():
    res = ticket_service.create_ticket()
    return res
