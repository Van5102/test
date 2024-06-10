from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import sessionmaker
from flask_socketio import SocketIO
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()
ma = Marshmallow()
socketio = SocketIO()