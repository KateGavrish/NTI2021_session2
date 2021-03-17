from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    middle = StringField('Отчество', validators=[DataRequired()])
    email = StringField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])

    submit = SubmitField('Войти')


class EditPassword(FlaskForm):
    old_password = PasswordField('текущий пароль', validators=[DataRequired()])
    new_password = PasswordField('новый пароль', validators=[DataRequired()])
    submit = SubmitField('Изменить')


class DeleteForm(FlaskForm):
    password = PasswordField('для удаления аккаунта введите пароль', validators=[DataRequired()])
    submit = SubmitField('Удалить')