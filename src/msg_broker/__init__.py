import asyncio
import json
import ast

import nats
import time

from src.device_payment.device_payment_service import create_device_payment


class Broker:

    def __init__(self):
        asyncio.run(self.subscriber())

    @staticmethod
    async def subscriber():
        # Connect to NATS!
        nc = await nats.connect(servers=['nats://144.91.119.81:4222'])

        while True:
            # Receive messages on 'foo'
            sub = await nc.subscribe("payment")

            # Process a message
            msg = await sub.next_msg()
            data = json.loads(msg.data.decode('ascii'))

            if msg.subject == 'payment':
                Broker.payment(
                    device_code=data['id'],
                    price=data['price'],
                    currency=data['currency'],
                    type=data['type']
                )

            # Close NATS connection
            # await nc.close()
            time.sleep(20)

    @staticmethod
    def payment(device_code, price, currency, type):
        # CREATE PAYMENT ON SERVICE
        create_device_payment(
            device_code=device_code,
            price=price,
            currency=currency,
            type=type
        )


