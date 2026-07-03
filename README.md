# 💰 Expense Tracker API

A secure and scalable Expense Tracker REST API built using **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Alembic**, and **JWT Authentication**.

---

## 🚀 Features

- User Registration
- User Login
- JWT Authentication
- Protected Routes
- Category Management
- Expense Management
- Dashboard Summary
- PostgreSQL Database
- Alembic Migrations
- SQLAlchemy ORM

---

## 🛠 Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- Passlib (bcrypt)
- JWT Authentication
- Python

---

## 📂 Project Structure

```
src/
│
├── database/
├── models/
├── routers/
├── schemas/
├── services/
├── utils/
└── main.py
```

---

## 📌 API Endpoints

### Authentication

- POST /auth/register
- POST /auth/login
- GET /auth/me

### Categories

- POST /categories/
- GET /categories/
- PUT /categories/{id}
- DELETE /categories/{id}

### Expenses

- POST /expenses/
- GET /expenses/
- PUT /expenses/{id}
- DELETE /expenses/{id}

### Dashboard

- GET /dashboard/

---

## ▶️ Run Locally

```bash
git clone <repository-url>

cd expense-tracker-api

python -m venv env

env\Scripts\activate

pip install -r requirements.txt

alembic upgrade head

fastapi dev src/main.py
```

---

## 👨‍💻 Author

**Piyush Sharma**

Backend Developer | Python | FastAPI | PostgreSQL