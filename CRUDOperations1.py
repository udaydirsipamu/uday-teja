from flask import Flask, request, render_template, redirect

from Models1 import EmployeeModel1, db

import os


class Config1:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Password%401@localhost:3306/test"
    SQLALCHEMY_TRACK_NOTIFICATIONS = False

app = Flask(__name__)
app.config.from_object(Config1)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/data/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template('InsertRecord.html')
    elif request.method == "POST":
        employee_id = request.form['employee_id']
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']

        empObj = EmployeeModel1(employee_id=employee_id, name=name, age=age, position=position)
        db.session.add(empObj)
        db.session.commit()
        return ("Record inserted Successfully")
@app.route("/data/getAll")
def getAll():
    employees = EmployeeModel1.query.all()
    return render_template("DisplayData.html", employees=employees)
@app.route("/data/upgrade/<int:id>", methods=["GET", "POST"])
def updateRecord(id):
    employee = EmployeeModel1.query.filter_by(employee_id=id).first()
    if request.method == "GET":
        return render_template("UpdateRecord.html", employee=employee)
    elif request.method == "POST":
        employee.employee_id = request.form['employee_id']
        employee.name = request.form['name']
        employee.age = request.form['age']
        employee.position = request.form['position']
        db.session.commit()

        return redirect("/data/getAll")
@app.route("/data/delete/<int:id>")
def deleteRecord(id):
    employee = EmployeeModel1.query.filter_by(employee_id=id).first()

    if employee:
        db.session.delete(employee)
        db.session.commit()
        return redirect("/data/getAll")


app.run(debug=True)