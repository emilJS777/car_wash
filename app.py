from src import app, socketio

# context_initializer.Initializer()
if __name__ == '__main__':
    socketio.run(app, debug=True)
