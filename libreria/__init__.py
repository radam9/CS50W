from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '6273c7823adbb51baa20d062c368f12a639e145548f0ca10'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://oijlbnofzvlluw:b06ac42f7be0fc4c1427c3c010323d6034387520cca39fdca8f9a7400ac3cdb9@ec2-54-247-72-30.eu-west-1.compute.amazonaws.com:5432/deuk0ndr5rg90v'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from libreria import routes, errors
