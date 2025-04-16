# Flask Project Starter Template

## Description
This project serves as a basic template for Flask applications. It allows you to quickly start working on a new application with a predefined folder structure, files, and essential dependencies.

## .env
The project uses a .env file to manage sensitive information. Add the following variable to the file:
SECRET_KEY=your_secret_key_here
Replace your_secret_key_here with a secure and unique key.

## Directory Structure

flaskTemplate/
├── .gitignore          # Ignored files and directories
├── .env                # Environment variables (not versioned)
├── requirements.txt    # Project dependencies
├── app.py              # Main Flask application file
├── routes/             # Application routes module
│   ├── __init__.py
│   └── routes.py
├── templates/          # HTML templates
│   └── index.html
└── __pycache__/        # Python temporary files (ignored)