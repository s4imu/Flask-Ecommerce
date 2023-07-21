from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///market.db"
db.init_app(app)
app.static_folder = 'static'

from market import routes