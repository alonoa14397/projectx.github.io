import os

class Config:
    SECRET_KEY = 'your_secret_key_here'
    DEBUG = True  # Set to False in production
    # Add more configuration options as needed

    # Example database configuration for SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Path to the JSON data files
    DATA_FOLDER = os.path.join(os.path.dirname(__file__), 'app', 'data')

    # You can define other constants or configuration settings here
