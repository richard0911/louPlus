import os
import json
from random import randint
from faker import Faker
from simpledu.models import db, User, Course, Chapter


fake = Faker()


def iter_user():
    return User(
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

def iter_chapter():
    for course in Course.query:
        for i in range(randint(3, 10)):
            yield Chapter(
                name=fake.sentence(),
                course=course,
                vedio_url='https://labfile.oss.aiyuncs.com/courses/923/week2-mp4/2-1-1-mac.mp4',
                vedio_duration='{}:{}'.format(randint(10, 30), randint(10, 59))
            )

def run():
    user = iter_user()
    db.session.add(user)

    for course in iter_courses():
        db.session.add(course)

    for chapter in iter_chapter():
        db.session.add(chapter)

    try:
        db.session.commit()
    except Exception as ex:
        print(ex)
        db.session.rollback()


