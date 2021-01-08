from slack import WebClient
from speedy import speedyBot
from slackeventsapi import SlackEventAdapter
import pymongo
import logging
import os

DATABASE = "speedy_mensajes"

# app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(
    os.environ['SLACK_SIGNING_SECRET'], endpoint="/slack/eventos")
slack_web_client = WebClient(token=os.environ['SLACK_TOKEN'])
onboarding_tutorials_sent = {}


def start_onboarding(user_id: str, channel: str):
    # Create a new onboarding tutorial.
    speedy_bot = speedyBot(channel)

    # Get the onboarding message payload
    message = speedy_bot.get_message_payload()

    # Post the onboarding message in Slack
    response = slack_web_client.chat_postMessage(**message)

    # Capture the timestamp of the message we've just posted so
    # we can use it to update the message after a user
    # has completed an onboarding task.
    speedy_bot.timestamp = response["ts"]

    # Store the message sent in onboarding_tutorials_sent
    if channel not in onboarding_tutorials_sent:
        onboarding_tutorials_sent[channel] = {}
    onboarding_tutorials_sent[channel][user_id] = speedy_bot


def start_onboarding_text(channel: str, text: str):
    # Create a new onboarding tutorial.
    message = {
        "channel": channel,
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": text
                }
            }
        ]
    }
    slack_web_client.chat_postMessage(**message)


def get_doc(mensaje):
    doc = {
        "type": mensaje["type"],
        "text": mensaje["text"],
        "ts": mensaje["ts"]
    }
    return doc


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


client = pymongo.MongoClient('localhost', 27017)
databases = client.list_database_names()

if DATABASE not in (databases):
    db = client[DATABASE]
    mensajes = slack_web_client.conversations_history(channel="C01CQ057JM8")
    for mensaje in mensajes['messages']:
        collection = db[mensaje['user']]
        doc = get_doc(mensaje)
        collection.insert_one(doc)


@ slack_events_adapter.on("message")
def message(payload):
    #Inicio mongo
    client = pymongo.MongoClient('localhost', 27017)
    db = client[DATABASE]

    #Obtención de evento
    event = payload.get("event", {})
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")
    

    #Ver si es alguna de las consultas de último mensaje o cuantos mensajes
    if "último mensaje" in text or "cúantos mensajes" in text:
        user = find_between(text, '@', '>')
        print("El usuario es este: ",user)
        collection = db[user]
        user_name = slack_web_client.users_info(user=user)['user']['name']
        if "último mensaje" in text:
            doc = collection.find().sort('ts', -1)
            texto = doc[0]['text']
            response = ("El último mensaje de @" + user_name + " es: " + texto)
        else:
            count = collection.find().count()
            response = ("La cantidad de mensajes de @" + user_name + " es: " + str(count))
        start_onboarding_text(channel_id, response)   
    #Si le dicen Hello, le contesta con Hola
    if text and text.lower() == "hello":
        return start_onboarding(user_id, channel_id)

    #Guarda el mensaje que recién llegó
    doc = get_doc(event)
    collection = db[user_id]
    collection.insert_one(doc)

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    slack_events_adapter.start(port=3000)
