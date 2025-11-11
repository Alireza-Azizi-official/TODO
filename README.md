**OverView**

A simple and lightweight TODO API built with FastAPI and MongoDB Atlas.
This project demonstrates CRUD operations using FastAPI and PyMongo, including both soft and hard delete features.
In this small project you will learn how to config Mongodb with FastAPI and how to work with it.


## Features

Create, read, update, and delete tasks

Soft delete (mark as deleted without removing from DB)

Hard delete (permanent removal)

MongoDB Atlas integration

Pydantic models for data validation


## Structure
Simple and modular structure


├── config.py


├── main.py


├── models.py


├── schemas.py


##  **Clone**
Clone the repository
git clone https://github.com/yourusername/fastapi-todo.git
cd fastapi-todo


## **Create a virtual environment**
```bash
- python -m venv venv
- source venv/bin/activate   (on Linux/Mac)
- venv\Scripts\activate      (on Windows)
```

## **Install dependencies**

```bash
pip install fastapi pymongo "uvicorn[standard]" bson
```

## Run the Application
```bash
uvicorn main:app --reload
```

## Then open your browser or API client at:
```bash
http://127.0.0.1:8000/docs
```