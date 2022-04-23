import asyncio
from src import app
from src._general.utils import context_initializer
import threading

<<<<<<< HEAD
context_initializer.Initializer()
# threading.Thread(target=msg_broker.main).start()

=======
# context_initializer.Initializer()
>>>>>>> origin/master
if __name__ == '__main__':
    # ON SERVER 5003
    app.run(debug=True, port=5002)
