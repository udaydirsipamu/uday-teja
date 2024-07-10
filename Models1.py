from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class EmployeeModel1(db.Model):
    __tablename__ = "Employee_python_mysql"

    employee_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(35))
    age = db.Column(db.Integer())
    position = db.Column(db.String(35))

    def __init__(self, employee_id, name, age, position):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.position = position
    def __repr__(self):
        return f"{self.employee_id} -- {self.name} -- {self.age} -- {self.position}"
