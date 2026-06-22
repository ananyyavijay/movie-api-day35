# 🎬 Movie API – FastAPI + SQLite + Azure App Service

A RESTful Movie Management API built with **FastAPI**, **SQLAlchemy**, and **SQLite**, featuring automated testing with **Pytest**, CI/CD using **GitHub Actions**, and deployment to **Azure App Service**.

---

## 🚀 Features

* Create a movie
* List all movies
* Get a movie by ID
* Filter movies by genre
* Health check endpoint
* SQLite database integration
* SQLAlchemy ORM
* Pydantic request/response validation
* Automated testing with Pytest
* CI pipeline using GitHub Actions
* CD pipeline with Azure App Service deployment

---

## 🛠️ Tech Stack

* Python 3.11
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Pytest
* GitHub Actions
* Azure App Service

---

## 📂 Project Structure

```text
movie-api/
│
├── main.py
├── database.py
├── models/
│   └── item.py
├── routers/
│   └── items.py
├── schemas/
│   └── item.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_movies.py
│
├── requirements.txt
└── .github/
    └── workflows/
        ├── ci.yml
        └── cd.yml
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd movie-api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## 📌 API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

### Create Movie

```http
POST /movies
```

Request:

```json
{
  "title": "Inception",
  "year": 2010,
  "genre": ["Action", "Sci-Fi"],
  "rating": 4.8
}
```

### Get All Movies

```http
GET /movies
```

### Filter Movies by Genre

```http
GET /movies?genre=Action
```

### Get Movie by ID

```http
GET /movies/{id}
```

---

## 🧪 Running Tests

Execute all tests:

```bash
pytest tests/ -v
```

Test coverage includes:

* Health endpoint returns 200
* POST creates movie and returns 201
* GET returns movie list
* GET by ID returns movie
* GET by ID returns 404 for missing movie

---

## 🔄 CI Pipeline

The CI workflow automatically runs on:

* Push to any branch
* Pull requests to main

Steps:

1. Checkout repository
2. Set up Python
3. Install dependencies
4. Run Pytest suite

---

## ☁️ Azure Deployment

The application is deployed to Azure App Service using GitHub Actions.

Deployment workflow:

```text
Push to main
        ↓
Run Tests
        ↓
Deploy to Azure App Service
        ↓
Application Live
```

---

## 🔐 GitHub Secrets

Required repository secret:

```text
AZURE_WEBAPP_PUBLISH_PROFILE
```

Contains the Azure App Service publish profile XML.

---

## 👩‍💻 Author

Ananya Vijay

B.Tech Electronics & Computer Science Engineering

KIIT University
