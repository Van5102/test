from flask import Flask
from flask_cors import CORS
from src.extentsion import *
from .constant.config import *

from .routes.product import user_route

def create_app():
    app = Flask(__name__)
    app.config.from_object(APP_CONFIG)
    socketio.init_app(app, cors_allowed_origins="*")
    jwt.init_app(app)
    db.init_app(app)
    CORS(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(user_route)

    return app