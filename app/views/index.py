# views/index.py
from flask import Blueprint, render_template
from app.controllers.imgbotconfig_controller import get_imgbotconfig_value

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/')
def index():
    # Example of fetching data from controller to pass to template
    welcome_message = get_imgbotconfig_value('welcome_message')
    return render_template('index.html', welcome_message=welcome_message)
