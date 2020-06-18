from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    x = {"nome": "Hello world"}
    print(jsonify(x))
    return "Hello"

if __name__ == '__main__':
    app.run()

