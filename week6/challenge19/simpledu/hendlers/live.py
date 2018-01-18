from flask import Blueprint, render_template
from simpledu.decorators import admin_required

live = Blueprint('live', __name__, url_prefix='/live')


@live.route('/')
def index():
	return render_template('live/live_page.html')


@live.route('/manage')
@admin_required
def manage():
	return render_template('live/manage.html')
