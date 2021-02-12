from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flas_mail import Mail
from flask_jwt_extended import JWTMail



db = SQLAlchemy()
migrate = Migrate()
mail = Mail()