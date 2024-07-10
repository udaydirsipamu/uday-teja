from flask import Flask, request
from flask_restful import Resource,Api
from Models import BookModel,db
from flask_cors import CORS
import os

app = Flask(__name__)

CORS(app)

api = Api(app)

class Config1:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Password%401@localhost:3306/test"
    SQLALCHEMY_TRACK_NOTIFICATIONS = False

app.config.from_object(Config1)

db.init_app(app)
with app.app_context():
    db.create_all()
class Book(Resource):
    def get(self):
        bookData = BookModel.query.all()
        return [{'id': book.id, 'title': book.title, 'author': book.author, 'cost': book.cost} for book in bookData]
class BookByID(Resource):
    def get(self, id):
        book = BookModel.query.get_or_404(id)
        return  {'id': book.id, 'title': book.title, 'author': book.author, 'cost': book.cost}
    def post(self,id):
        id = request.json["id"]
        title = request.json["title"]
        author = request.json["author"]
        cost = request.json["cost"]

        book = BookModel(id=id, title=title, author=author, cost=cost)
        db.session.add(book)
        db.session.commit()
        return "Book data inserted in the db Successfully",200
    def put(self, id):
        book = BookModel.query.get_or_404(id)

        if book:
            book.title = request.json["title"]
            book.author = request.json["author"]
            book.cost = request.json["cost"]
            db.session.commit()
            return "Given record is updated in the db successfully"
        else:
            return "Given record is not found in the db.."

    def delete(self, id):
        book = BookModel.query.get_or_404(id)
        db.session.delete(book)
        db.session.commit()

        return "Given book is deleted Successfully in the db",200

api.add_resource(Book, "/book/")

api.add_resource(BookByID, "/book/<int:id>")

app.run(debug=True)