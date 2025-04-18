Employee Management System - 3-Hour Challenge

Overview

This project is a Flask-based web application designed to:

Generate synthetic employee data

Store and manage data in PostgreSQL

Expose REST APIs for data retrieval and analytics

Visualize employee data using Chart.js dashboard

Implement bonus features like CSV export, API rate limiting, and logging

Built within a 3-hour coding challenge, the project focuses on clarity, modularity, and speed.

Features

Employee, Department, Attendance, Performance, and Salary models

Data generation with Faker

PostgreSQL database integration

REST API Endpoints with Swagger UI documentation

Chart.js-based visualization dashboard

CSV Export functionality

API request logging and error logging

Rate limiting using Flask-Limiter

Health check and basic unit testing

Technologies Used

Python 3.11

Flask

Flask-SQLAlchemy

PostgreSQL

Flasgger (Swagger UI)

Chart.js (Frontend dashboard)

Faker (Synthetic data generation)

Flask-Limiter (API rate limiting)

Python Unittest (Basic API testing)

Folder Structure

Glynac.ai/
├── app.py # Flask app setup
├── config.py # Configuration settings
├── extensions.py # SQLAlchemy and Limiter instances
├── models.py # Database models
├── routes.py # API routes and logic
├── templates/
│ └── dashboard.html # Chart.js dashboard
├── test_app.py # Basic unit tests
├── requirements.txt # Project dependencies
├── .env # Environment variables (DB config)
└── logs/
└── api.log # API logs

Setup Instructions

1. Clone the repository

git clone <your-repository-link>
cd Glynac.ai

2. Create and activate virtual environment

python3 -m venv env
source env/bin/activate

3. Install requirements

pip install -r requirements.txt

4. Set up PostgreSQL Database

Create a PostgreSQL database

Add DB credentials to .env file:

DATABASE_URL=postgresql://username:password@localhost/databasename

5. Run the app

python app.py

Visit:

Swagger UI at: http://127.0.0.1:5000/apidocs/

Dashboard at: http://127.0.0.1:5000/dashboard

6. Run tests

python test_app.py

Important API Endpoints

Endpoint

Purpose

/generate-data

Generate synthetic employees and related data

/employees

List all employees with filters and pagination

/departments

List all departments

/performance/<employee_id>

Get performance record for an employee

/summary

System summary (total employees, attendance, etc.)

/attendance-rate

Attendance data per employee

/performance-distribution

Performance rating distribution

/export-employees

Export employee data as downloadable CSV

/dashboard

Visual dashboard built with Chart.js

/health

Health check of the system

Bonus Features Implemented

API rate limiting using Flask-Limiter

CSV export functionality

API request and error logging

Chart.js dashboard with live data and refresh button

Last updated timestamp on dashboard

Basic unit test on health endpoint

Design and Architecture

For detailed architecture explanation and design choices, see:

design_decisions.md

Note

This project is meant for educational purposes. Production deployment would require Dockerization, production-level rate limiting, authentication mechanisms, and advanced testing.

Author

Shanmukh Sitaram GApril 20253-Hour Challenge Submission

Thank You!
