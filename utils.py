def parse_heroku(f):
    if f.get("resource") == "build":
        c = None
        if f.get("action") == "update":
            title = "Build complete"
            description = "Heroku has finished deploying a new version of ChessCord. The bot should now be back online, although restoring full functionality might take about a minute."
            color = 0x1ABC9C
        else:
            title = "New build started"
            description = "Heroku has started deploying a new version of ChessCord. The bot will be down for a few minutes while the new version is starting up."
            color = 0xE74C3C
    else:
        c = f'ChessCord is currently `{f.get("data").get("state")}`...'
        if f.get("action") == "destroy":
            title = "ChessCord shutting down"
            description="ChessCord is being terminated. This is most likely part of a daily restart or a new build, and the bot will come back online soon."
            color = 0xE74C3C
        elif f.get("action") == "create":
            title = "ChessCord starting up"
            description="ChessCord is now starting up and will be online shortly."
            color = 0xE67E22
        else:
            title = "ChessCord is back online"
            description="ChessCord should now be online, although restoring full functionality might take about a minute."
            color = 0x1ABC9C
    data = {
        "content": c,
        "embeds": [
            {
                "author": {
                    "NameError": "Heroku",
                    "icon_url": "https://i.ibb.co/gjDdGpD/heroku.png"
                },
                "title": title,
                "description": description,
                "color": color,
                "thumbnail": {
                    "url": "https://images.discordapp.net/avatars/811760473422823465/4d2e470acfc0be5ce75fbc23b406c6ce.png?size=1024"
                }
            }
        ]
    }
    return data
    # return c, create_embed(
    #     title,
    #     description,
    #     special_author["Heroku", "https://i.ibb.co/gjDdGpD/heroku.png"],
    #     color=color
    # )