# views/sales.py
from flask import Blueprint, render_template

bp = Blueprint('sales', __name__, url_prefix='/sales')

@bp.route('/')
def sales():
    # Example view function for the sales page
    return render_template('sales.html')
