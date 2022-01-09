import requests

from flask import Flask, request

from utils import parse_heroku
from bot import send_msg

app = Flask(__name__)

@app.route("/")
def index():
    return "ChessCord Webhooks is up and running..."


@app.route("/heroku", methods=["POST"])
def heroku():
    f = request.json
    data = parse_heroku(f)
    url = "https://discord.com/api/webhooks/928901900286439465/OB1eH1lPd23USGJLRJdGlN-mdzPUB69X1NN-X81E953b9IpnhqQEbj3eNnxbWxvz7q7A"
    requests.post(url, json=data)
    return ""


def run_webserver():
    app.run(host="0.0.0.0", port=8080)
