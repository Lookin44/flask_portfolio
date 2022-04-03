from flask import Flask, render_template, url_for


app = Flask(__name__)

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
    }
]


@app.route('/')
def start_page():
    return render_template(
        'start_page.html',
        blogs=blogs,
        title='Главная страница'
    )


@app.route('/about')
def about_page():
    return render_template(
        'about_page.html',
        title='Об авторе'
    )


if __name__ == '__main__':
    app.run(debug=True)
