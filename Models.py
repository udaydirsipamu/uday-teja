from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BookModel(db.Model):
    __tablename__ = "Books_Flask_Restful_SQLAlchemy"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(35))
    author = db.Column(db.String(35))
    cost = db.Column(db.Integer())

    def __init__(self, id, title, author, cost):
        self.id = id
        self.title = title
        self.author = author
        self.cost = cost
