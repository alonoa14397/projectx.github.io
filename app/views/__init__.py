# views/__init__.py
from flask import Blueprint

# Import your view modules
from .about_us import bp as about_us_bp
from .features import bp as features_bp
from .index import bp as index_bp
from .login import bp as login_bp
from .management import bp as management_bp
from .sales import bp as sales_bp

# Register Blueprints
def register_blueprints(app):
    app.register_blueprint(about_us_bp)
    app.register_blueprint(features_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(management_bp)
    app.register_blueprint(sales_bp)

# Optionally, you can call the register_blueprints function to automatically register
# all the blueprints when this module is imported.
# For example, if you have a Flask app instance named `app`, you can do:
# from views import register_blueprints
# register_blueprints(app)
