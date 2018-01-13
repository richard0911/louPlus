from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, Required
from simpledu.models import db, User
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
