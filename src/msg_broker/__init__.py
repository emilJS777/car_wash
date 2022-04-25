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


        while True:
            # Connect to NATS!
            nc = await nats.connect(servers=['nats://144.91.119.81:4222'])

            # Receive messages on 'foo'
            sub = await nc.subscribe("payment")

            # Publish a message to 'foo'
            # await nc.publish("powerOffOn", bytes(json.dumps({'id': '1', 'price': 400, 'currency': 'amd', 'type': 'coin'})
            #                                       .encode('utf-8')))a

            # Process a message
            try:
                msg = await sub.next_msg()
                data = json.loads(msg.data.decode('ascii'))
                print(msg)
                if msg.subject == 'payment':
                    print(data)
                    Broker.payment(
                        device_code=data['id'],
                        price=data['price'],
                        currency=data['currency'],
                        type=data['type']
                    )
            except:
                pass

            finally:
                # Close NATS
                await nc.close()
                time.sleep(3)




    @staticmethod
    def payment(device_code, price, currency, type):
        # CREATE PAYMENT ON SERVICE
        create_device_payment(
            device_code=device_code,
            price=price,
            currency=currency,
            type=type
        )



