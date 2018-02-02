from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig

app = Flask(__name__)
Bootstrap(app)
db = SQLAlchemy(app)
app.config.from_object(DevelopmentConfig)

from route import *

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.run()