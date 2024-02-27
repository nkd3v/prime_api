from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "Hi, hello"


@app.route('/is_prime/<int:num>', methods=['GET'])
def is_prime(num):
    if num <= 1:
        return "false"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "false"
    return "true"


if __name__ == '__main__':
    app.run()