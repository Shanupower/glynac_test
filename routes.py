from flask import Blueprint, jsonify,request,render_template
from faker import Faker
from models import db, Employee, Department, Attendance, Performance, Salary
import random
from datetime import datetime, timedelta

routes = Blueprint('routes', __name__)
fake = Faker()
@routes.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')
@routes.route('/attendance-rate', methods=['GET'])
def attendance_rate():
    """
    Employee Attendance Rate
    ---
    tags:
      - Attendance
    summary: Returns attendance (present/absent counts) for each employee
    responses:
      200:
        description: Attendance data per employee
    """
    employees = Employee.query.all()
    output = []

    for emp in employees:
        present_days = Attendance.query.filter_by(employee_id=emp.id, status='Present').count()
        absent_days = Attendance.query.filter_by(employee_id=emp.id, status='Absent').count()
        output.append({
            "employee": f"{emp.first_name} {emp.last_name}",
            "present_days": present_days,
            "absent_days": absent_days
        })

    return jsonify(output)
@routes.route('/salary-summary', methods=['GET'])
def salary_summary():
    """
    Salary Summary for Employees
    ---
    tags:
      - Salary
    summary: Returns salary breakdown (base, bonus, deductions) for each employee
    responses:
      200:
        description: Salary data per employee
    """
    salaries = Salary.query.all()
    output = []

    for sal in salaries:
        employee = Employee.query.get(sal.employee_id)
        output.append({
            "employee": f"{employee.first_name} {employee.last_name}",
            "base_salary": round(sal.base_salary, 2),
            "bonus": round(sal.bonus, 2),
            "deductions": round(sal.deductions, 2)
        })

    return jsonify(output)
@routes.route('/performance-distribution', methods=['GET'])
def performance_distribution():
    """
    Performance Rating Distribution
    ---
    tags:
      - Performance
    summary: Returns count of employees per performance rating
    responses:
      200:
        description: Distribution of performance ratings
    """
    distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    performances = Performance.query.all()
    for perf in performances:
        if perf.rating in distribution:
            distribution[perf.rating] += 1

    return jsonify(distribution)

@routes.route('/summary', methods=['GET'])
def get_summary():
    """
    Get System Summary (for Visualization)
    ---
    tags:
      - Summary
    summary: Returns aggregated employee, department, attendance, and performance data
    description: Useful for visualizing employee distribution, attendance, and performance metrics.
    responses:
      200:
        description: Summary data for dashboard visualization
    """
    total_employees = Employee.query.count()

    departments = Department.query.all()
    department_summary = {}
    for dept in departments:
        count = Employee.query.filter_by(department_id=dept.id).count()
        department_summary[dept.name] = count

    performances = Performance.query.all()
    if performances:
        avg_rating = round(sum(p.rating for p in performances) / len(performances), 2)
    else:
        avg_rating = 0

    present_count = Attendance.query.filter_by(status='Present').count()
    absent_count = Attendance.query.filter_by(status='Absent').count()

    return jsonify({
        "total_employees": total_employees,
        "departments": department_summary,
        "average_performance_rating": avg_rating,
        "attendance_summary": {
            "Present": present_count,
            "Absent": absent_count
        }
    })
@routes.route('/employees', methods=['GET'])
def list_employees():
    """
    List Employees
    ---
    tags:
      - Employees
    parameters:
      - name: page
        in: query
        type: integer
        required: false
        description: Page number (pagination)
      - name: limit
        in: query
        type: integer
        required: false
        description: Number of employees per page
      - name: department_id
        in: query
        type: integer
        required: false
        description: Filter employees by Department ID
    responses:
      200:
        description: List of employees returned successfully
    """
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    department_id = request.args.get('department_id', type=int)

    query = Employee.query

    if department_id:
        query = query.filter_by(department_id=department_id)

    pagination = query.paginate(page=page, per_page=limit, error_out=False)
    employees = pagination.items

    return jsonify({
        "total": pagination.total,
        "page": page,
        "limit": limit,
        "data": [
            {
                "id": emp.id,
                "first_name": emp.first_name,
                "last_name": emp.last_name,
                "email": emp.email,
                "department": emp.department.name if emp.department else None
            } for emp in employees
        ]
    })

@routes.route('/departments', methods=['GET'])
def list_departments():
    """
    List Departments
    ---
    tags:
      - Departments
    responses:
      200:
        description: List of departments returned successfully
    """
    departments = Department.query.all()
    return jsonify([
        {
            "id": dept.id,
            "name": dept.name,
            "location": dept.location,
            "manager": dept.manager
        } for dept in departments
    ])

@routes.route('/performance/<int:employee_id>', methods=['GET'])
def employee_performance(employee_id):
    """
    Get Employee Performance Record
    ---
    tags:
      - Performance
    parameters:
      - name: employee_id
        in: path
        type: integer
        required: true
        description: Employee ID to retrieve performance record
    responses:
      200:
        description: Performance record returned successfully
    """
    performance = Performance.query.filter_by(employee_id=employee_id).first()
    if not performance:
        return jsonify({"error": "No performance record found."}), 404

    return jsonify({
        "employee_id": performance.employee_id,
        "review_date": performance.review_date.isoformat(),
        "reviewer": performance.reviewer,
        "rating": performance.rating,
        "comments": performance.comments
    })
@routes.route('/generate-data', methods=['GET'])
def generate_data():
    """
    Generate Synthetic Data
    ---
    tags:
      - Utility
    summary: Regenerates synthetic employee data after clearing existing records
    description: This endpoint will delete all existing departments, employees, attendance, performance, and salary records before generating new synthetic data.
    responses:
      200:
        description: Synthetic data generated successfully
    """
    Salary.query.delete()
    Attendance.query.delete()
    Performance.query.delete()
    Employee.query.delete()
    Department.query.delete()
    db.session.commit()

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

    db.session.commit()

    # Step 3: Create new employees
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

    db.session.commit()

    # Step 4: Create attendance, performance, salary records
    for emp in employees:
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

        performance = Performance(
            employee_id=emp.id,
            review_date=fake.date_between(start_date='-1y', end_date='today'),
            reviewer=fake.name(),
            rating=random.randint(1,5),
            comments=fake.sentence(nb_words=10)
        )
        db.session.add(performance)

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
