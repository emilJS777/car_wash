from src import mqtt
import json
from . import device_mqtt


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('car_wash/device/#')


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    # GET DATA AND ASSIGN DATA JSON FORMAT
    data = dict(topic=message.topic, payload=json.loads(message.payload.decode()))

    # IF TOPIC DEVICE ERROR
    if data['topic'] == 'car_wash/device/error':
        device_mqtt.device_error(data=data['payload'])

    # IF TOPIC DEVICE PAYMENT CASH
    if data['topic'] == 'car_wash/device/payment/cash':
        device_mqtt.device_payment_cash(data=data['payload'])

