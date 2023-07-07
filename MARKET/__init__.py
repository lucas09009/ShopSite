from flask import Flask
import os
import random
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


ShopSite = Flask(__name__)

from .config import Config
ShopSite.config.from_object(Config)

ShopSite.config['SECRET_KEY'] = random._urandom(56)
ShopSite.config['DEBUG'] = True

basedir = os.path.abspath(os.path.dirname(__file__))

# Configuration de la base de données PostgreSQL
db_info = {
    'host': 'localhost',
    'database': 'Market',
    'psw': 'bayernmunich',
    'user': 'postgres',
    'port': '5432'
}

ShopSite.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}:{db_info['port']}/{db_info['database']}"
ShopSite.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(ShopSite)
migrate = Migrate(ShopSite, db)
from MARKET import Routes
