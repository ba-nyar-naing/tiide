from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/banyar")
def banyar():
    return "Ba Nyar Naing"
