from threading import Thread
import os

from dotenv import load_dotenv

from bot import client
from app import run_webserver

load_dotenv()

webserver = Thread(target=run_webserver)
webserver.start()

client.run(os.getenv("TOKEN"))
