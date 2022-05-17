from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required

from blog import app, db, bcrypt
from blog.form import RegistrationForm, LoginForm, ProfileEditForm, NewPostForm
from blog.models import User, Post
from blog.services import get_all_posts
from blog.utilites import save_picture


@app.route('/')
def index():
    all_posts = get_all_posts()
    return render_template(
        'post_card.html',
        posts=all_posts,
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
        flash('Вы уже авторизированны', 'info')
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
    logout_user()
    flash('Вы вышли из своего аккаунта', 'info')
    return redirect(url_for('login'))


@app.route('/account')
@login_required
def account():
    image_file = url_for(
        'static',
        filename='profile_pict/' + current_user.image_file
    )
    return render_template(
        'account.html',
        title='Профиль',
        image_file=image_file
    )


@app.route('/account/account_edit', methods=['GET', 'POST'])
@login_required
def account_edit():
    form = ProfileEditForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.name = form.name.data
        current_user.last_name = form.last_name.data
        current_user.user_email = form.user_email.data
        current_user.about = form.about.data
        db.session.commit()
        flash('Вы обновили свой аккаунт', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.last_name.data = current_user.last_name
        form.user_email.data = current_user.user_email
        form.about.data = current_user.about
    return render_template(
        'account_edit.html',
        title='Редактирование профиля',
        form=form
    )


@app.route('/post/new', methods=('GET', 'POST'))
@login_required
def post_new():
    form = NewPostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            author=current_user
        )
        db.session.add(post)
        db.session.commit()
        flash('Вы опубликовали свой пост', 'success')
        return redirect(url_for('index'))
    return render_template(
        'edit_post.html',
        title='Новый пост',
        form=form,
        legend='Новый пост'
    )
