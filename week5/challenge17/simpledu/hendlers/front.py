from flask import Blueprint, render_template
from ..models import Course
from simpledu.forms import LoginFrom, RegisterFrom


front = Blueprint('front', __name__)


@front.route('/')
def index():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)


@front.route('/login')
def login():
    form = LoginFrom()
    return render_template('login.html', form=form)


@front.route('/register')
def register():
    form = RegisterFrom()
    return render_template('register.html', form=form)
