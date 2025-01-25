from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config.from_prefixed_env(prefix="FLASK") # For this we need to install python-dotenv

import os
baseDir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(baseDir,'cogniquest.sqlite3')

db = SQLAlchemy(app)
jwt = JWTManager(app)
ma = Marshmallow(app)
app.app_context().push()  # This is required to create the tables in the database