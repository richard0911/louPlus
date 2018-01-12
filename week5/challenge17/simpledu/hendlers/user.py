from flask import Blueprint, render_template
from ..models import User, Course

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/<username>')
def show_user_info(username):
    user_info = User.query.filter(User.username == username).first()
    courses = Course.query.filter(Course.author_id == user_info.id).all()
    return render_template('user_info.html', user=user_info, courses=courses)
