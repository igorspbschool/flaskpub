from flask import Flask
#библиотека для передачи запроса чере WSGI сервер
from waitress import serve

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


if __name__ == '__main__':
    # app.run(port=8080, host='0.0.0.0')
    serve(app, host='0.0.0.0', port=8080)