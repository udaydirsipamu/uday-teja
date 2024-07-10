from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "project_user"

    id=db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(55), unique=True,nullable=False)
    firstname = db.Column(db.String(55),nullable=False)
    lastname = db.Column(db.String(55),nullable=False)
    emailid = db.Column(db.String(55),unique=True,nullable=False)
    password = db.Column(db.String(55),nullable=False)

class AppointmentModel(db.Model):
    __tablename__="project_app"

    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    service = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)