from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def hello():
    return jsonify(message="hey, it's backend!")


@app.route("/solve", methods=["POST"])
def solve():
    print("Solving")
    return jsonify(message="post ok !")


if __name__ == "__main__":
    app.run(debug=True)
