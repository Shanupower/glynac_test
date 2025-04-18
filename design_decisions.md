# Architecture & Design Explanation

## Overview

This project is a Flask-based web application that:

- Generates synthetic employee data
- Stores it in PostgreSQL
- Exposes REST APIs for data retrieval
- Visualizes key analytics using Chart.js
- Adds bonus features like CSV export, API rate limiting, and logging

The primary goal was to build a scalable, modular, and clean system within a 3-hour challenge.

---

## Technologies Used

| Technology                        | Purpose                                               |
| :-------------------------------- | :---------------------------------------------------- |
| **Flask**                         | Web application framework                             |
| **SQLAlchemy**                    | ORM to interact with PostgreSQL                       |
| **PostgreSQL**                    | Relational database for storing employee data         |
| **Flasgger**                      | Auto-generate Swagger UI for API documentation        |
| **Chart.js**                      | Frontend visualization of employee metrics            |
| **Flask-Limiter**                 | Apply API rate limiting and prevent abuse             |
| **Python Unittest**               | Basic unit testing for health check                   |
| **Logging (RotatingFileHandler)** | Record API requests and errors to a log file          |
| **dotenv**                        | Load database configuration securely from `.env` file |

---

## Architecture Choices

| Component                  | Decision                                                                                  |
| :------------------------- | :---------------------------------------------------------------------------------------- |
| **Flask App Factory**      | Simple single-app setup for speed and clarity                                             |
| **Modular Code**           | `models.py`, `routes.py`, `config.py`, `extensions.py` to maintain separation of concerns |
| **Database Design**        | 5 models: Employee, Department, Attendance, Performance, Salary                           |
| **Synthetic Data**         | Used `Faker` to create realistic dummy data for quick testing                             |
| **REST APIs**              | Clean endpoints for employees, departments, performance records, summary analytics        |
| **Swagger Documentation**  | Integrated Flasgger for interactive API testing                                           |
| **Frontend Visualization** | Built a simple `/dashboard` using Chart.js to plot live data                              |
| **Error Handling**         | Added minimal error checks during database operations                                     |
| **Logging**                | Request and error logs saved to rotating log files for auditability                       |
| **Rate Limiting**          | Limited critical endpoints like `/generate-data` to prevent misuse                        |

---

## Folder Structure

```
Glynac.ai/
├── app.py                # Flask app initialization
├── config.py              # Environment configurations
├── extensions.py          # SQLAlchemy and Limiter instance
├── models.py              # SQLAlchemy models
├── routes.py              # All API routes and logic
├── templates/
│   ├── dashboard.html     # Chart.js dashboard
├── test_app.py            # Unit tests
├── requirements.txt       # Python package dependencies
├── .env                   # Database credentials
└── logs/
    └── api.log            # API request and error logs
```

---

## Key Reasoning Behind Choices

- **Flask over Django**: Faster to set up for a lightweight API + frontend app.
- **Separate `extensions.py`**: Avoid circular imports when using `db`, `limiter`, etc.
- **Direct app routes and Swagger**: Quick visualization and API interaction without building a heavy frontend.
- **SQLAlchemy models**: Make database interaction easy, scalable, and portable.
- **Chart.js dashboard**: No external frontend framework needed; minimal overhead.
- **Faker data generation**: Simulate realistic employee data without manual entry.
- **Rotating logs**: Keep log files manageable and ready for production practices.
- **Testing health endpoint**: Ensure basic system health check before scaling testing.

---

## Bonus Features Added

- CSV Export (`/export-employees`)
- Rate Limiting on critical routes (`Flask-Limiter`)
- Logging of API requests and errors
- Responsive Chart.js dashboard with Refresh functionality
- Last updated timestamp on dashboard
- Basic Unit Tests for `/health` API

---
