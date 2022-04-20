from src import app
from src._general.utils import context_initializer


# context_initializer.Initializer()
if __name__ == '__main__':
    # ON SERVER 5003
    app.run(debug=True, port=5002)
