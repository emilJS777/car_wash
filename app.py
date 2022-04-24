import asyncio
from src import app, msg_broker
from src._general.utils import context_initializer
import threading

# context_initializer.Initializer()
threading.Thread(target=msg_broker.Broker).start()
if __name__ == '__main__':
    # ON SERVER 5003

    app.run(debug=True, port=5003)
