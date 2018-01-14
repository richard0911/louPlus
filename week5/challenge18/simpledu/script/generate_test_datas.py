import os
import json
from random import randint
from faker import Faker
from simpledu.models import db, User, Course, Chapter


fake = Faker()


def iter_user():
    yield User(
        username='Jack Lee',
        email='jacklee@example.com',
        password='zxcvbnm',
        job='研发工程师'
    )


def iter_courses():
    author = User.query.filter_by(username='Jack Lee').first()
    with open(os.path.join(os.path.dirname(__file__), '..', 'datas', 'courses.json')) as f:
        courses = json.load(f)

    for course in courses:
        yield Course(
            name=course['name'],
            description=course['description'],
            image_url=course['image_url'],
            author=author
        )


