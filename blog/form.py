from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import (
    StringField,
    TextAreaField,
    PasswordField,
    SubmitField,
    BooleanField
)
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    EqualTo,
    ValidationError
)

from blog.models import User


class RegistrationForm(FlaskForm):
    name = StringField(
        'Имя',
        validators=[
            DataRequired(message='Поле не может быть пустым'),
            Length(
                min=4,
                max=20,
                message='Поле должно содержать от 2-ух до 20-ти символов'
            ),
        ]
    )
    last_name = StringField(
        'Фамилия',
        validators=[
            DataRequired(message='Поле не может быть пустым'),
            Length(min=2, max=20),
        ]
    )
    user_email = StringField(
        'Электронная почта',
        validators=[
            DataRequired(message='Поле не может быть пустым'),
            Email(message='Некорректный адрес электронной почты')
        ]
    )
    password = PasswordField(
        'Пароль',
        validators=[
            DataRequired(message='Поле не может быть пустым'),
        ]
    )
    pass_password = PasswordField(
        'Повторите пароль',
        validators=[
            DataRequired(message='Поле не может быть пустым'),
            EqualTo('password', message='Пароли не сходятся')
        ]
    )
    submit = SubmitField('Регистрация')

    def validate_user_email(self, email):
        user_email = User.query.filter_by(user_email=email.data).first()
        if user_email:
            raise ValidationError('Этот адрес уже зарегистрирован')


class LoginForm(FlaskForm):
    user_email = StringField(
        'Электронная почта',
        validators=[
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField(
        'Пароль',
        validators=[
            DataRequired()
        ]
    )
    remember = BooleanField(
        'Запомнить меня'
    )
    submit = SubmitField(
        'Войти',
        default=False
    )


class ProfileEditForm(FlaskForm):
    name = StringField(
        'Имя',
        validators=[
            DataRequired(message='Поле не может быть пустым'),
            Length(
                min=4,
                max=20,
                message='Поле должно содержать от 2-ух до 20-ти символов'
            ),
        ]
    )
    last_name = StringField(
        'Фамилия',
        validators=[
            DataRequired(message='Поле не может быть пустым'),
            Length(min=2, max=20),
        ]
    )
    user_email = StringField(
        'Электронная почта',
        validators=[
            DataRequired(message='Поле не может быть пустым'),
            Email(message='Некорректный адрес электронной почты')
        ]
    )
    about = TextAreaField(
        'О себе'
    )
    submit = SubmitField('Сохранить')

    def validate_user_email(self, email):
        if email.data != current_user.user_email:
            user_email = User.query.filter_by(user_email=email.data).first()
            if user_email:
                raise ValidationError('Этот адрес уже зарегистрирован')
