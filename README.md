# ChessCord Webhooks

Handles Webhook interactions between services like Discord, Heroku, and Top.gg

## Features

### Heroku
Receives Heroku webhooks regarding the state of ChessCord, modifies the content, and sends them as a Discord Webhook.

## Implementation

 - `python` - The programming language used
     - `flask` - Used to run the webserver
     - `requests` - For sending webhook requests