from flask import Flask, request, jsonify
import logging
from waitress import serve

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!!!"



if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)