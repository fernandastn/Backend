from flask import Flask
from .config import Config
from .extensions import db, migrate

from .cardapio.model import Cardapio
from .bebidas.model import Bebidas
from .sucos.model import Sucos

from app.cardapio.controllers import cardapio_api
from app.bebidas.controllers import bebidas_api
from app.sucos.controllers import sucos_api


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(cardapio_api)
    app.register_blueprint(bebidas_api)
    app.register_blueprint(sucos_api)

    return app


        