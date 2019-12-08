import os, pymysql
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)

user=os.getenv('MYSQL_USER')
password=os.getenv('MYSQL_PASSWORD')
host=os.getenv('MYSQL_HOST')
db=os.getenv('MYSQL_DATABASE')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(user, password, host, db)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db=SQLAlchemy()
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application import routes


