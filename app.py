from src import app, socketio
from src.utils import context_initializer

# context_initializer.Initializer()
if __name__ == '__main__':
    socketio.run(app, debug=True)
