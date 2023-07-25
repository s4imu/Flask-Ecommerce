from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///market.db"
app.config["SECRET_KEY"] = '870b211fe0dc289fbe933a48'
db.init_app(app)
brcypt = Bcrypt(app)
login_manager.init_app(app)
app.static_folder = 'static'

from market import routes