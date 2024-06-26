# views/about_us.py
from flask import Blueprint, render_template
from app.controllers.settings_controller import get_setting_value

bp = Blueprint('about_us', __name__, url_prefix='/about-us')

@bp.route('/')
def about_us():
    # Example of fetching data from controller to pass to template
    company_name = get_setting_value('company_name')
    return render_template('about_us.html', company_name=company_name)
