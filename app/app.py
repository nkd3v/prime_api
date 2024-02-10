
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "It works!"


@app.route('/getcode', methods=['GET'])
def getcode(name):
    return "123456"


if __name__ == '__main__':
    app.run()
