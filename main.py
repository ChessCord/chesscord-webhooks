from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "ChessCord Webhooks is up and running..."

@app.route("/heroku", methods=["POST"])
def heroku():
    f = request.json
    print(f)
    if f.get("resource") == "build":
        if f.get("action") == "update":
            title = "New build started"
            description = "Heroku has started deploying a new version of ChessCord, prepare for some downtime"
        else:
            title = "Build complete"
            description = "Heroku has finished deploying a new version of ChessCord, the bot should be back online"
    else:
        if f.get("action") == "destroy":
            title = "ChessCord shutting down"
            description="ChessCord is being terminated, and will be restarted shortly"
        elif f.get("action") == "create":
            title = "ChessCord starting up"
            description="ChessCord is now starting and will be online shortly"
        else:
            title = "ChessCord is back online"
            description="ChessCord should now be online, and full functionality should be restored in less than a minute"
    data = {
        "content": f'ChessCord is currently `{f.get("data").get("state")}`...',
        "embeds": [
            {
                "author": {
                    "NameError": "Heroku",
                    "icon_url": "https://i.ibb.co/gjDdGpD/heroku.png"
                },
                "title": title,
                "description": description
            }
        ],
        "thumbnail": {
            "url": "https://images.discordapp.net/avatars/811760473422823465/4d2e470acfc0be5ce75fbc23b406c6ce.png?size=1024"
        },
        "footer": {
            "url": "https://img.icons8.com/material-outlined/344/info.png",
            "text": "This message was automatically generated by Heroku, and sent through ChessCord Webhooks"
        }
    }
    url = "https://discord.com/api/webhooks/928901900286439465/" + "OB1eH1lPd23USGJLRJdGlN-mdzPUB69X1NN-X81E953b9IpnhqQEbj3eNnxbWxvz7q7A"
    requests.post(url, json=data)
    return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
