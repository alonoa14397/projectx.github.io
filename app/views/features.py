# views/features.py
from flask import Blueprint, render_template

bp = Blueprint('features', __name__, url_prefix='/features')

@bp.route('/')
def features():
    # Example view function for the features page
    return render_template('features.html')
