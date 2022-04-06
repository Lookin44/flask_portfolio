from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField
)
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    name = StringField(
        'Имя',
        validators=[
            DataRequired(),
            Length(
                min=2,
                max=20,
                message='Введите не меньше 2 и не больше 20 букв.'
            )
        ]
    )
    last_name = StringField(
        'Фамилия',
        validators=[
            DataRequired(),
            Length(
                min=2,
                max=20,
                message='Введите не меньше 2 и не больше 20 букв.'
            )
        ]
    )
    user_email = StringField(
        'Электронная почта',
        validators=[
            DataRequired(),
            Email(message='Вы должны ввести адрес электронной почты.')
        ]
    )
    password = PasswordField(
        'Пароль',
        validators=[
            DataRequired(message='Это обязательное поле.')
        ]
    )
    pass_password = PasswordField(
        'Подтвердите пароль',
        validators=[
            DataRequired(),
            EqualTo('password', message='Пароли не сходятся.')
        ]
    )
    submit = SubmitField('Мои данные верны')


class LoginForm(FlaskForm):
    user_email = StringField(
        'Электронная почта',
        validators=[
            DataRequired(),
            Email(message='Вы должны ввести адрес электронной почты.')
        ]
    )
    password = PasswordField(
        'Пароль',
        validators=[
            DataRequired()
        ]
    )
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
