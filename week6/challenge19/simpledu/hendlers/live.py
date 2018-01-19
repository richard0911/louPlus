from flask import Blueprint, render_template, current_app, request, flash, redirect, url_for
from simpledu.decorators import admin_required
from simpledu.models import LiveInfo
from simpledu.forms import LiveForm


live = Blueprint('live', __name__, url_prefix='/live')


@live.route('/live_page')
def index():
	return render_template('live/live_page.html')


@live.route('/')
@admin_required
def manage():
	page = request.args.get('page', default=1, type=int)
	pagination = LiveInfo.query.paginate(
		page=page,
		per_page=current_app.config['INDEX_PER_PAGE'],
		error_out=False
	)
	return render_template('live/live.html', pagination=pagination)


@live.route('/create_live', methods=['GET', 'POST'])
@admin_required
def create_live():
	form = LiveForm()
	if form.validate_on_submit():
		form.create_live()
		flash('直播创建成功', 'success')
		return redirect(url_for('live.manage'))
	return render_template('live/create_live.html', form=form)
