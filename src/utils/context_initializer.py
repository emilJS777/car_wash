from src import logger
from src.ticket import ticket_service_db
from src.role import role_service_db
from src.ticket.ticket_model import Ticket


class Initializer:
    roles = ["admin", "engineer", "owner", "client"]

    # CONSTRUCTOR
    def __init__(self):
        self.init_roles()
        self.init_first_ticket()

    def init_roles(self):
        # CREATE SELF ROLES IF NOT EXIST
        for role_name in self.roles:
            if not role_service_db.get_role_by_name(name=role_name):
                role_service_db.create_role(name=role_name)
                logger.info(f"role by name {role_name} successfully created")

    def init_first_ticket(self):
        # IF FIRST TICKET NOT FOUND
        if not Ticket.query.first():
            # GET ID ADMIN ROLE
            role_id = role_service_db.get_role_by_name(name=self.roles[0]).id
            # GENERATE TICKET CODE
            ticket_code = ticket_service_db.generate_ticket_code()
            # CREATE TICKET BY ADMIN ROLE
            ticket_service_db.create_ticket(role_id=role_id, code=ticket_code)
            logger.info(f"ticket for first admin created! code={ticket_code}")
