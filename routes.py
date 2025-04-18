from flask import Blueprint, jsonify
from faker import Faker
from models import db, Employee, Department, Attendance, Performance, Salary
import random
from datetime import datetime, timedelta

routes = Blueprint('routes', __name__)
fake = Faker()

@routes.route('/generate-data', methods=['GET'])
def generate_data():
    departments = ['Engineering', 'Marketing', 'Sales', 'Finance', 'HR']
    dept_objs = []
    for name in departments:
        dept = Department(
            name=name,
            location=fake.city(),
            manager=fake.name()
        )
        db.session.add(dept)
        dept_objs.append(dept)
    
    employees = []
    for _ in range(5):
        dept = random.choice(dept_objs)
        employee = Employee(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.unique.email(),
            phone=fake.phone_number(),
            date_of_birth=fake.date_of_birth(minimum_age=25, maximum_age=50),
            date_joined=fake.date_between(start_date='-5y', end_date='today'),
            department=dept
        )
        db.session.add(employee)
        employees.append(employee)

    for emp in employees:
        # Attendance
        for day in range(5):
            attendance = Attendance(
                employee_id=emp.id,
                date=datetime.now().date() - timedelta(days=day),
                status=random.choice(['Present', 'Absent']),
                check_in_time=fake.time_object(),
                check_out_time=fake.time_object(),
                remarks=fake.sentence(nb_words=6)
            )
            db.session.add(attendance)

        # Performance
        performance = Performance(
            employee_id=emp.id,
            review_date=fake.date_between(start_date='-1y', end_date='today'),
            reviewer=fake.name(),
            rating=random.randint(1,5),
            comments=fake.sentence(nb_words=10)
        )
        db.session.add(performance)

        # Salary
        salary = Salary(
            employee_id=emp.id,
            base_salary=random.uniform(50000,120000),
            bonus=random.uniform(5000,15000),
            deductions=random.uniform(1000,5000),
            payment_date=fake.date_this_month(),
            payment_method=random.choice(['Bank Transfer', 'Cheque'])
        )
        db.session.add(salary)

    db.session.commit()
    return jsonify({"status": "success", "message": "Synthetic data generated successfully!"})


def register_routes(app):
    """Register all blueprints and future routes here."""
    app.register_blueprint(routes)
