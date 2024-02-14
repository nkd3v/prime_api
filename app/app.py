from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "It works!"


@app.route('/getcode', methods=['GET'])
def getcode():
    return "_"


@app.route('/plus/<num1>/<num2>', methods=['GET'])
def plus(num1, num2):
    return str(eval(f'{num1} + {num2}'))


if __name__ == '__main__':
    app.run()
