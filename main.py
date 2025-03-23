from flask import Flask

app = Flask(__name__)

@app.route('/carousel')
def mars():
    return '''<!doctype html>
                <html lang="ru">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Пейзажи Porsche</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
                </head>
                <body>
                    <div class="container mt-4">
                        <h1 class="text-center">Пейзажи Porsche</h1>
                        <div id="porscheCarousel" class="carousel slide" data-bs-ride="carousel">
                            <div class="carousel-inner">
                                <div class="carousel-item active">
                                    <img src="/static/porshe1.jpeg" class="d-block w-100" alt="porshe 1">
                                </div>
                                <div class="carousel-item">
                                    <img src="/static/porshe2.jpeg" class="d-block w-100" alt="porshe 2">
                                </div>
                                <div class="carousel-item">
                                    <img src="/static/porshe3.jpeg" class="d-block w-100" alt="porshe 3">
                                </div>
                            </div>
                        </div>
                    </div>
                </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')