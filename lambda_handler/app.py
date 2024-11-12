import awsgi
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello", methods=["GET"])
def hello_get():
    return {"msg": "get method"}


@app.route("/hello", methods=["POST"])
def hello_post():
    return {"msg": "post method"}


def lambda_handler(event, context):
    return awsgi.response(app, event, context)
