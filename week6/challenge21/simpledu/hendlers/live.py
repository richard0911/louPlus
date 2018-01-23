from flask import Blueprint, render_template, current_app, request, flash, redirect, url_for
from simpledu.decorators import admin_required
from simpledu.models import LiveInfo
from simpledu.forms import LiveForm


live = Blueprint('live', __name__, url_prefix='/live')


@live.route('/')
def index():
	live_info = LiveInfo.query.first()
	return render_template('live/live_page.html', live_info=live_info)


@live.route('/create_live', methods=['GET', 'POST'])
@admin_required
def create_live():
	form = LiveForm()
	if form.validate_on_submit():
		form.create_live()
		flash('直播创建成功', 'success')
		return redirect(url_for('admin.manage'))
	return render_template('live/create_live.html', form=form)
