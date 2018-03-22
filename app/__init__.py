from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "pineapple"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:Pineapple123@localhost/userdb"


db = SQLAlchemy(app)

UPLOAD_FOLDER = './app/static/uploads'


app.config.from_object(__name__)
from app import views
