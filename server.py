from flask import Flask

app = Flask(__name__)


@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def apple():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def present():
    return '''<!doctype html>
            <html lang='ru'>
            <head>
                <meta charset='utf-8'>
            </head>
            <body>
                <p>Человечество вырастает из детства.</p>
                <p>Человечеству мала одна планета.</p>
                <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
                <p>И начнем с Марса!</p>
                <p>Присоединяйся!</p>
            </body>
            </html>'''


@app.route('/image_mars')
def image_mars():
    return '''<!doctype>
                <html lang="ru">
                <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                </head>
                <body>
                    <p><strong>Жди нас, Марс!</strong></p>
                    <img src="/static/image/mars.jpeg" alt="Марс закрыт для зрителей">
                    <p>Вот она какая, красная планета.</p>
                </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
