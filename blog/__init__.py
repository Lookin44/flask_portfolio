from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_pyfile('../settings.py')

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from blog import routes
