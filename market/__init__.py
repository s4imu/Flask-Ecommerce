from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///market.db"
app.config["SECRET_KEY"] = '870b211fe0dc289fbe933a48'
db.init_app(app)
brcypt = Bcrypt(app)
app.static_folder = 'static'

from market import routes