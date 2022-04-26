import asyncio
import json
import ast

from nats.aio.client import Client as NATS
from nats.aio.errors import ErrTimeout
import time

from src.device_payment.device_payment_service import create_device_payment
from src.device.device_service import update_device_content
from src.device import device_service_db


class Broker:
    def __init__(self):
        asyncio.run(Broker.subscriber())

    @staticmethod
    def payment(data):
        # CREATE PAYMENT ON SERVICE
        create_device_payment(
            device_code=data['id'],
            price=data['price'],
            currency=data['currency'],
            type=data['type']
        )

    @staticmethod
    def content(data):
        # UPDATE CONTENT LATHER & WATER
        update_device_content(
            device_code=data['id'],
            water=data['water'],
            lather=data['lather']
        )


    async def message_handler(msg):
        subject: str = msg.subject
        data = json.loads(msg.data.decode())

        # CHECK ACTIVE DEVICE
        device = device_service_db.get_device_by_code(data['id'])
        if device and not device.active:
            device_service_db.activate_device(device.id)

        if subject == "payment":
            Broker.payment(data)

        elif subject == "content":
            Broker.content(data)


    @staticmethod
    async def subscriber():
        nc = NATS()

        while True:
            await nc.connect(servers=["nats://144.91.119.81:4222"])

            await nc.subscribe("payment", cb=Broker.message_handler)
            await nc.subscribe("content", cb=Broker.message_handler)
            await nc.flush()

            # await nc.publish("updates", json.dumps({"symbol": "GOOG", "price": 1200}).encode())
            await asyncio.sleep(1)
            await nc.close()


# class Broker:
#
#     def __init__(self):
#         asyncio.run(self.subscriber())
#
#     @staticmethod
#     async def subscriber():
#
#
#         while True:
#             # Connect to NATS!
#             nc = await nats.connect(servers=['nats://144.91.119.81:4222'])
#
#             # Receive messages on 'foo'
#             # await nc.subscribe("payment")
#
#
#             # Publish a message to 'foo'
#             # await nc.publish("powerOffOn", bytes(json.dumps({'id': '1', 'price': 400, 'currency': 'amd', 'type': 'coin'})
#             #                                       .encode('utf-8')))a
#
#             # Process a message
#             try:
#                 future = asyncio.Future()
#
#                 async def cb(msg):
#                     nonlocal future
#                     future.set_result(msg)
#
#                 await nc.subscribe("payment", cb=cb)
#                 await nc.flush()
#
#                 # Wait for message to come in
#                 msg = await asyncio.wait_for(future, 1)
#                 subject = msg.subject
#                 data = json.loads(msg.data.decode('ascii'))
#
#
#                 if subject == "payment":
#                     Broker.payment(data=data)
#
#                 if subject == "content":
#                     Broker.content(data=data)
#
#
#                 # msg = await sub.next_msg()
#                 # data = json.loads(msg.data.decode('ascii'))
#                 # print(msg)
#                 # if msg.subject == 'payment':
#                 #     print(data)
#                 #     Broker.payment(
#                 #         device_code=data['id'],
#                 #         price=data['price'],
#                 #         currency=data['currency'],
#                 #         type=data['type']
#                 #     )
#                 # if msg.subject
#             except:
#                 pass
#
#             finally:
#                 # Close NATS
#                 # await nc.close()
#                 time.sleep(3)
#
#
#     @staticmethod
#     def content(data):
#         print("content: ", data)


    # @staticmethod
    # def payment(data):
    #     # CREATE PAYMENT ON SERVICE
    #     print("payment: ", data)
    #     create_device_payment(
    #         device_code=data['id'],
    #         price=data['price'],
    #         currency=data['currency'],
    #         type=data['type']
    #     )



