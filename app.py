from src import app
from src.utils import context_initializer

context_initializer.Initializer()
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
