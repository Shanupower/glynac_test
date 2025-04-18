from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    location = db.Column(db.String(100))
    manager = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=db.func.now())

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(50))
    date_of_birth = db.Column(db.Date)
    date_joined = db.Column(db.Date)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    department = db.relationship('Department')
    created_at = db.Column(db.DateTime, default=db.func.now())

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    date = db.Column(db.Date)
    status = db.Column(db.String(10))  # Present/Absent
    check_in_time = db.Column(db.Time)
    check_out_time = db.Column(db.Time)
    remarks = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=db.func.now())

class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    review_date = db.Column(db.Date)
    reviewer = db.Column(db.String(100))
    rating = db.Column(db.Integer)  # 1 to 5
    comments = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=db.func.now())

class Salary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    base_salary = db.Column(db.Float)
    bonus = db.Column(db.Float)
    deductions = db.Column(db.Float)
    payment_date = db.Column(db.Date)
    payment_method = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=db.func.now())
