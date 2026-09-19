# Flask To-Do App

A simple To-Do web application built with Flask, SQLite and Flask-SQLAlchemy.

## Features

- User registration
- User login and logout
- Session-based authentication
- Add tasks
- View tasks
- Change task status
- Delete tasks
- User-specific tasks
- SQLite database

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- SQLite
- Jinja2
- HTML
- CSS

## Project Structure

```text
TODO_app/
│
├── app/
│   ├── routes/
│   │   ├── auth.py
│   │   └── tasks.py
│   │
│   ├── static/
│   │   ├── CSS/
│   │   └── js/
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── tasks.html
│   │
│   ├── __init__.py
│   └── models.py
│
├── .gitignore
├── requirements.txt
└── run.py
