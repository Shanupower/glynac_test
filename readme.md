# Employee Management System

Flask-based backend application for generating synthetic employee data, managing it with PostgreSQL, exposing APIs with Swagger UI, and visualizing analytics via Chart.js. Built within a 3-hour coding challenge focused on clarity, speed, and modular design.

---

## Project Features

This project includes:

- Synthetic data generation using Faker
- PostgreSQL database integration with SQLAlchemy ORM
- RESTful API endpoints documented via Swagger UI
- Chart.js frontend dashboard for visualizing employee data
- CSV export functionality
- API request and error logging with RotatingFileHandler
- API rate limiting using Flask-Limiter
- Basic unit tests for health checks

---

## Technologies Used

Python 3.11, Flask, SQLAlchemy, PostgreSQL, Flasgger (Swagger UI), Chart.js, Faker, Flask-Limiter, Python Unittest, dotenv

---

## Folder Structure

The main structure of the project:

- app.py: Flask app initialization
- config.py: Configuration settings
- extensions.py: SQLAlchemy and Limiter instance definitions
- models.py: Database models for Employee, Department, Attendance, Performance, Salary
- routes.py: All API endpoints and dashboard route
- templates/dashboard.html: Chart.js dashboard page
- test_app.py: Unit tests
- requirements.txt: Python dependencies
- .env: Environment variables (PostgreSQL connection)
- logs/api.log: API request and error logs

---

## Setup Instructions

Clone the repository:

git clone <your-repository-link>
cd Glynac.ai

Create and activate a virtual environment:

python3 -m venv env
source env/bin/activate

Install dependencies:

pip install -r requirements.txt

Create a PostgreSQL database locally and update your .env file:

DATABASE_URL=postgresql://username:password@localhost/databasename

Run the application:

python app.py

Swagger UI will be available at http://127.0.0.1:5000/apidocs/
Dashboard will be available at http://127.0.0.1:5000/dashboard

Run unit tests:

python test_app.py

---

## Important Endpoints

- /generate-data: Generate synthetic data (employees, departments, attendance, performance)
- /employees: List employees with pagination and filtering
- /departments: List all departments
- /performance/<employee_id>: Get an employee's performance record
- /summary: System overview (employee count, attendance summary)
- /attendance-rate: Attendance rate per employee
- /performance-distribution: Performance rating distribution
- /export-employees: Download employee data as a CSV file
- /dashboard: Visual dashboard
- /health: System health check

---

## Bonus Features

- CSV Export functionality
- API Request and Error Logging
- Rate Limiting using Flask-Limiter
- Refreshable and animated Chart.js dashboard
- Last Updated timestamp display
- Unit Testing for /health endpoint

---

## Architecture & Design

Modular design using separate files for models, routes, configurations, and extensions.
Swagger UI is integrated for quick API testing.
Frontend visualization is kept lightweight using Chart.js directly via a simple HTML template.
Rate limiting and logging add extra robustness for production-readiness.

Full explanation available in design_decisions.md.

---

## Author

Built by Shanmukh Sitaram — April 2025 — for 3-Hour Coding Challenge.

---

# Thank You!
