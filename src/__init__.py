from .config import app, db, logger, mail, socketio

# routes
from .auth import auth_routes
from .car_wash import car_wash_routes
from .device import device_routes
from .device_error import device_error_routes
from .device_payment import device_payment_routes
from .email import email_routes
from .role import role_routes
from .ticket import ticket_routes
from .user import user_routes
from .loyal_card import loyal_card_routes
from .loyal_card_payment import loyal_card_payment_routes
from .devcie_counter import device_counter_routes


# from src._old.mqtt import *
