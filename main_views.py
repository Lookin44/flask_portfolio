from flask import Flask, render_template, url_for
from form import RegistrationForm, LoginForm


app = Flask(__name__)
app.config.from_pyfile('settings.py')


blogs = [
    {
        'author': 'Egor Lukin',
        'title': 'Первый пост',
        'content': 'Тестовый пост',
        'date_created': '28.03.2022'
    },
    {
        'author': 'Egor Lukin',
        'title': 'Второй пост',
        'content': 'Тестовый пост №2',
        'date_created': '29.03.2022'
    },
    {
        'author': 'Egor Lukin',
        'title': 'Второй пост',
        'content': 'Тестовый пост №3',
        'date_created': '30.03.2022'
    },
    {
        'author': 'Egor Lukin',
        'title': 'Второй пост',
        'content': 'Тестовый пост №5',
        'date_created': '01.04.2022'
    },
]


@app.route('/')
def index():
    return render_template(
        'start_page.html',
        blogs=blogs,
        title='Главная страница'
    )


@app.route('/about')
def about():
    return render_template(
        'about_page.html',
        title='Об авторе'
    )


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    return render_template(
        'registration.html',
        title='Регистрация',
        form=form
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template(
        'login.html',
        title='Войти',
        form=form
    )
