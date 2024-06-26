# views/management.py
from flask import Blueprint, render_template

bp = Blueprint('management', __name__, url_prefix='/management')

@bp.route('/')
def management():
    # Example view function for the management page
    return render_template('management.html')
