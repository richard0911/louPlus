from flask import Blueprint, render_template, request, current_app, flash, url_for, redirect
from simpledu.decorators import admin_required
from simpledu.models import Course, db, User, LiveInfo
from simpledu.forms import CoursesFrom, UserFrom, SysMsgForm


admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/')
@admin_required
def admin_index():
    return render_template('admin/index.html')


@admin.route('/courses')
@admin_required
def courses():
    page = request.args.get('page', default=1, type=int)
    pagination = Course.query.paginate(
        page=page,
        per_page=current_app.config['INDEX_PER_PAGE'],
        error_out=False
    )
    return render_template('admin/courses.html', pagination=pagination)


@admin.route('/courses/create', methods=['GET', 'POST'])
@admin_required
def create_course():
    form = CoursesFrom()
    if form.validate_on_submit():
        form.create_course()
        flash('课程创建成功', 'success')
        return redirect(url_for('admin.courses'))
    return render_template('admin/create_course.html', form=form)


@admin.route('/courses/<int:course_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)
    form = CoursesFrom(obj=course)
    if form.validate_on_submit():
        form.update_course(course)
        flash('课程更新成功')
        return redirect(url_for('admin.courses'))
    return render_template('admin/edit_course.html', form=form, course=course)


@admin.route('/courses/<int:course_id>/delete', methods=['GET', 'POST'])
@admin_required
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    flash('课程删除成功', 'success')
    return redirect(url_for('admin.courses'))


@admin.route('/user')
@admin_required
def users():
    page = request.args.get('page', default=1, type=int)
    pagination = User.query.paginate(
        page=page,
        per_page=current_app.config['INDEX_PER_PAGE'],
        error_out=False
    )
    return render_template('admin/users.html', pagination=pagination)


@admin.route('/user/create_user', methods=['GET', 'POST'])
@admin_required
def create_user():
    form = UserFrom()
    if form.validate_on_submit():
        form.create_user()
        flash('用户创建成功', 'success')
        return redirect(url_for('admin.users'))
    return render_template('admin/create_user.html', form=form)


@admin.route('/user/<int:user_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    form = UserFrom(obj=user)
    if form.validate_on_submit():
        form.update_user(user)
        flash('用户更新成功', 'success')
        return redirect(url_for('admin.users'))
    return render_template('admin/edit_user.html', form=form, user=user)


@admin.route('/user/<int:user_id>/delete', methods=['GET', 'POST'])
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('用户删除成功', 'success')
    return redirect(url_for('admin.users'))


@admin.route('/live')
@admin_required
def manage():
	page = request.args.get('page', default=1, type=int)
	pagination = LiveInfo.query.paginate(
		page=page,
		per_page=current_app.config['INDEX_PER_PAGE'],
		error_out=False
	)
	return render_template('live/live.html', pagination=pagination)


@admin.route('/message', methods=['GET', 'POST'])
@admin_required
def sendsysmsg():
    form = SysMsgForm()
    if form.validate_on_submit():
        form.send()
        flash('发送成功', 'sucess')
        return redirect(url_for('admin.sendsysmsg'))
    return render_template('live/sys_msg.html', form=form)