from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "pineapple"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:Pineapple123@localhost/userdb"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://mlgrsqdyybzxnu:f361e4400806c6c92fb832dc1e196cb4e213f906ffeba7ffbc0a6c8bb64aeb81@ec2-23-21-217-27.compute-1.amazonaws.com:5432/derlilg3evp6ko"


db = SQLAlchemy(app)

UPLOAD_FOLDER = './app/static/uploads'


app.config.from_object(__name__)
from app import views
