from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import Length, Email, EqualTo, Required, URL, NumberRange
from simpledu.models import db, User, Course, LiveInfo
from wtforms import ValidationError


class RegisterFrom(FlaskForm):
    username = StringField('Username', validators=[Required(), Length(3, 24, message='The Username should be 3 to 24 word')])
    email = StringField('Email', validators=[Required(), Email(message='illegal Email ')])
    password = PasswordField('Password', validators=[Required(), Length(6, 24, message='Input is wrong')])
    repeat_password = PasswordField('Password Again', validators=[Required(), EqualTo('password', message='The two passwords are inconsistent')])
    submit = SubmitField('Sibmit')

    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('The Username had exist')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('The Email had exist')


class LoginFrom(FlaskForm):
    username = StringField('Username', validators=[Required(), Length(3, 24)])
    password = PasswordField('PassWord', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('Remenber me')
    submit = SubmitField('Submit')

    def validate_username(self, field):
        if field.data and not User.query.filter_by(username=field.data).first():
            raise ValidationError('The account did not exists!')

    def validate_password(self, field):
        user = User.query.filter_by(username=self.username.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('Wrong password')


class CoursesFrom(FlaskForm):
    name = StringField('课程名称', validators=[Required(), Length(5, 32)])
    description = TextAreaField('课程简介', validators=[Required(), Length(20, 256)])
    image_url = StringField('封面图片', validators=[Required(), URL()])
    author_id = IntegerField('作者ID', validators=[Required(), NumberRange(min=1, message='无效的用户ID')])
    submit = SubmitField('提交')

    def validate_author_id(self, filed):
        if not User.query.get(self.author_id.data):
            raise ValidationError('用户不存在')

    def create_course(self):
        course = Course()
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course

    def update_course(self, course):
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course


class UserFrom(FlaskForm):
    username = StringField('用户名称', validators=[Required(), Length(3, 24)])
    email = StringField('邮箱', validators=[Required(), Email(message='illegal Email ')])
    password = PasswordField('密码', validators=[Required(), Length(6, 24, message='Input is wrong')])
    submit = SubmitField('提交')

    def create_user(self):
        user = User()
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return user

    def update_user(self, user):
        self.populate_obj(user)
        db.session.add(user)
        db.commit()
        return user


class LiveForm(FlaskForm):
    name = StringField('直播名称', validators=[Required(), Length(3, 32)])
    username = StringField('直播用户', validators=[Required(), Length(3, 24)])
    submit = SubmitField('提交')

    def create_live(self):
        user_id = User.query.filter_by(username=self.username.data).first().id
        live_info = LiveInfo(user_id=user_id)
        self.populate_obj(live_info)
        db.session.add(live_info)
        db.session.commit()
        return live_info
