from src import logger
from src.services_db import ticket_service_db, role_service_db


class Initializer:
    roles = ["engineer", "client"]

    # CONSTRUCTOR
    def __init__(self):
        self.create_roles(roles=self.roles)
        self.create_first_ticket(role_title=self.roles[0])

    @staticmethod
    def create_roles(roles):
        # CHECK OR CREATE ROLE
        for title in roles:
            role = role_service_db.get_role_by_title(title=title)
            if not role:
                new_role = role_service_db.create_role(title=title)
                logger.info(f"new role by title {new_role.title} created")
            else:
                logger.info(f"role by title {title} exist")

    @staticmethod
    def create_first_ticket(role_title):
        # CHECK OR CREATE FIRST TICKET
        role = role_service_db.get_role_by_title(title=role_title)

        if not role:
            return logger.info(f"role by title {role_title} not found, to generate a ticket")

        elif ticket_service_db.get_ticket_by_role_id(role_id=role.id):
            return logger.info(f"ticket for role {role.title} exist")

        else:
            ticket = ticket_service_db.create_ticket(role_id=role.id)
            return logger.info(f"new ticket code successfully generated {ticket.code}")
