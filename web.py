from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/training/<prof>')
def sim(prof='Врач'):
    if 'инженер' in prof or 'строитель' in prof:
        sim = 'Инженерные тренажеры'
        image = '/static/image/Engineering.jpeg'
    else:
        sim = 'Научные симуляторы'
        image = '/static/image/Scientific.jpeg'
    return render_template('base.html', sim=sim, image=image)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')