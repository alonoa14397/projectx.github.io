# app/__init__.py

from flask import Flask

# Initialize Flask application
app = Flask(__name__)

# Example configuration settings (optional)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['DATA_FOLDER'] = '/path/to/your/data'

# Import views and models (assuming they are defined in separate modules)
from app import views  # Import views to register Blueprints
from app import models  # Import models to initialize database models (if using)

# Optionally, you can configure other aspects of your application here

