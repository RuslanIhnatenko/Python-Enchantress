from flask import Flask
from random import randint
app = Flask(__name__)


@app.route("/")
def main():
    return "Hello) Guess the number)"


@app.route('/num')
def hello():
    rn = randint(1, 10)
    return f'Is this your number {rn}?'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
