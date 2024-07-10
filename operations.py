from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from Models import User, AppointmentModel, db
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
api = Api(app)
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Password%401@localhost:3306/test"
    SQLALCHEMY_TRACK_NOTIFICATIONS = False

app.config.from_object(Config)

db.init_app(app)
with app.app_context():
    db.create_all()


class Login(Resource):
    def post(self):
        user_data=request.get_json()
        print("Received login request with data",user_data)
        username = user_data.get("username")
        password = user_data.get("password")
        if not username or not password:
            return jsonify({"message":"Username or password is missing"})
        user = User.query.filter_by(username=username,password=password).first()
        if user:
            print('Login successful for user',username)
            return jsonify({"message":"Login successful"})
        else:
            print("login failed",username)
            return jsonify({"message":"Username or password is incorrect"})

class Register(Resource):
    def post(self):
        user_data=request.get_json()
        username = user_data.get("username")
        firstname = user_data.get("firstname")
        lastname = user_data.get("lastname")
        emailid = user_data.get("emailid")
        password = user_data.get("password")

        if not username and not firstname and not lastname and not emailid and not password:
            return jsonify({"message":"Missing details"})

        user=User.query.filter_by(username=username).first() or User.query.filter_by(emailid=emailid).first()
        if user:
            return jsonify({"message": "Register user already exists"})
        user1 = User(username=username, firstname=firstname, lastname=lastname, emailid=emailid,password=password)
        db.session.add(user1)
        db.session.commit()
        return jsonify({"message": "User registered successfully"})

def is_slot_available(date,time,id=None):
    query=AppointmentModel.query.filter_by(date=date,time=time)
    if id:
        query=query.filter(AppointmentModel.id!=id)
    return query.count() == 0
class Appointment(Resource):
    def get(self):
        appointments=AppointmentModel.query.all()
        return [{'id':app.id,'name':app.name,'service':app.service,'date':app.date,
                 'time':app.time}for app in appointments]
    def post(self):
        name=request.json["name"]
        service=request.json["service"]
        date=request.json["date"]
        time=request.json["time"]

        if not name and not service and not date and not time:
            return jsonify({"message":"Missing details"})
        if not is_slot_available(date,time):
            return jsonify({"message":"Slot not available"})
        appointment=AppointmentModel(name=name,service=service,date=date,time=time)
        db.session.add(appointment)
        db.session.commit()
        return jsonify({"message":"Appointment booked successfully"})
class AppointmentById(Resource):
    def put(self,id):
        appointment=AppointmentModel.query.get_or_404(id)
        data=request.get_json()
        new_date=data["date"]
        new_time=data["time"]
        if not is_slot_available(new_date,new_time,id):
            return jsonify({"message":"Slot not available"})
        appointment.name=data["name"]
        appointment.service=data["service"]
        appointment.date=new_date
        appointment.time=new_time
        db.session.commit()
        return jsonify({"message":"Appointment details updated successfully"})
    def delete(self,id):
        appointment=AppointmentModel.query.get_or_404(id)
        db.session.delete(appointment)
        db.session.commit()
        return jsonify({"message":"Appointment cancelled successfully"})

api.add_resource(Appointment, "/appointment")
api.add_resource(AppointmentById, "/appointment/<int:id>")
api.add_resource(Login,"/login")
api.add_resource(Register, "/reg")
app.run(debug=True)