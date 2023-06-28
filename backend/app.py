from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "hey, it's backend!"


if __name__ == "__main__":
    app.run()
