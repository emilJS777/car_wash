from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from datetime import datetime
import logging
from flask_cors import CORS
from flask_mail import Mail
from flask_mqtt import Mqtt
from flask_socketio import SocketIO


app = Flask(__name__)
api = Api(app)

# CONNECT TO DATABASE CONFIG
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:<password>@localhost/car_wash_db"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../car_wash.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)
db.create_all()
migrate = Migrate(app, db)


# QR IMG FILE PATH
app.config["QR_IMG_PATH"] = "src/_img/qr"

# CONNECT JWT CONFIG
app.config["JWT_SECRET_KEY"] = "H^&67KCsn@77G"
app.config["JWT_ACCESS_EXP"] = 20
app.config["JWT_REFRESH_EXP"] = 3000
jwt = JWTManager(app)

# Set CORS options on app configuration
app.config['CORS_RESOURCES'] = {r"/*": {"origins": "*"}}
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, supports_credentials=True)

# LOGGING
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(f"{datetime.utcnow()}")

# EMAIL CONFIG
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'emil.hambardzumyan28@gmail.com'
app.config['MAIL_PASSWORD'] = '07454521'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# MQTT CONFIG
app.config['MQTT_CLIENT_ID'] = 'mqttx_db9f3db5'
app.config['MQTT_BROKER_URL'] = 'broker.emqx.io'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
# app.config['MQTT_KEEPALIVE'] = 5
# app.config['MQTT_TLS_ENABLED'] = False
mqtt = Mqtt(app)

socketio = SocketIO(app)
