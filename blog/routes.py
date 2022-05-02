from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required

from blog import app, db, bcrypt
from blog.form import RegistrationForm, LoginForm
from blog.models import User, Post

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
        'post_card.html',
        blogs=blogs,
        title='Главная страница',
        active='index'
    )


@app.route('/about')
def about():
    return render_template(
        'about_page.html',
        title='Контакты',
        active='about'
    )


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(
            form.password.data
        ).decode('UTF-8')
        user = User(
            name=form.name.data,
            last_name=form.last_name.data,
            user_email=form.user_email.data,
            password=hashed_pw
        )
        db.session.add(user)
        db.session.commit()
        flash(f'Аккаунт создан. Добро пожаловать {form.name.data}!', 'success')
        return redirect(url_for('login'))
    return render_template(
        'registration.html',
        title='Регистрация',
        form=form
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('Вы уже авторизированны', 'info')
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.user_email.data).first()
        if user and bcrypt.check_password_hash(
                user.password, form.password.data
        ):
            login_user(user, form.remember.data)
            next_page = request.args.get('next')
            flash('Вы авторизированны', 'info')
            return redirect(next_page) if next_page else redirect(
                url_for('index')
            )
        else:
            flash('Авторизация не пройдена. Проверьте адрес электронной почты '
                  'и пароль', 'danger')
    return render_template(
        'login.html',
        title='Войти',
        form=form
    )


@app.route('/logout')
def logout():
    if current_user.is_anonymous:
        flash('Вы не авторизированны', 'warning')
        return redirect(url_for('login'))
    logout_user()
    flash('Вы вышли из своего аккаунта', 'info')
    return redirect(url_for('login'))


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    if request.method == 'GET':
        image_file = url_for(
            'static',
            filename='profile_pict/' + current_user.image_file
        )
        return render_template(
            'account.html',
            title='Профиль',
            image_file=image_file
        )
    elif request.method == 'POST':
        pass
