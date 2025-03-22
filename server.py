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


@app.route('/promotion_image')
def advertising():
    return '''<!doctype html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                          crossorigin="anonymous">
                    <title>Колонизация/title>
                </head>
                <body>
                <h1>Жди нас, Марс!</h1>
                <img src="/static/image/mars.jpeg" alt="Марс закрыт для зрителей">
                
                <div class="alert" style="background-color: #dcdcdc; font-weight: bold;">
                    Человечество вырастает из детства.
                </div>
                <div class="alert" style="background-color: #c8e6c9; font-weight: bold;">
                    Человечеству мала одна планета.
                </div>
                <div class="alert" style="background-color: #e3f2fd; font-weight: bold;">
                    Мы сделаем обитаемыми безжизненные пока планеты.
                </div>
                <div class="alert" style="background-color: #fff9c4; font-weight: bold;">
                    И начнем с Марса!
                </div>
                <div class="alert" style="background-color: #f8bbd0; font-weight: bold;">
                    Присоединяйся!
                </div>
                </body>
                
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
