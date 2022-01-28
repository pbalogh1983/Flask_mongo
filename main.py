from flask import Flask

app = Flask(__name__)


@app.route("/")
def myfunc():
    return "<h1>Container test</h1>"



if __name__ == "__main__":
    app.run()