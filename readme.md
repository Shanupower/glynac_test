# Synthetic Employee Data API

This project is a **3-hour coding challenge** demonstrating quick decision-making, efficient coding practices, and clean architecture using Flask.

---

## 🎯 Core Objectives

- Generate synthetic employee data with Faker.
- Design PostgreSQL database models.
- Develop RESTful APIs using Flask.
- Document APIs via Swagger UI.

---

## 🛠 Technologies

- **Backend:** Flask, Flask-RESTful
- **Database:** PostgreSQL
- **Data Generation:** Faker
- **Documentation:** Swagger UI

---

## 🚀 Quick Setup

### Prerequisites

- Python 3.8+
- PostgreSQL

### Installation

```bash
git clone <your_repository_link>
cd employee-data-api
python -m venv env
source env/bin/activate
pip install -r requirements.txt
cp .env.example .env
flask db upgrade
python generate_data.py
flask run
```

---

## 📌 API Endpoints

- **`GET /employees`**: List employees.
- **`GET /employees/<id>/performance`**: Employee performance details.

Swagger documentation at `http://localhost:5000/swagger/`

---

## 📂 Project Structure

```
employee-data-api/
├── app.py
├── models.py
├── generate_data.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🔗 Submission

GitHub: `<your_repository_link>`
