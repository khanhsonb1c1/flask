from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mật Khẩu', validators=[DataRequired()])
    role_id = SelectField('Vai Trò', choices=[('1', 'Admin'), ('2', 'User')], validators=[DataRequired()])
    submit = SubmitField('Đăng Ký')
