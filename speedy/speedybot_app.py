from slack import WebClient
from speedy import speedyBot
from slackeventsapi import SlackEventAdapter
import logging
import os

#app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'], endpoint="/slack/event")
slack_web_client = WebClient(token=os.environ['SLACK_TOKEN'])
onboarding_tutorials_sent = {}

def start_onboarding(user_id: str, channel: str):
    # Create a new onboarding tutorial.
    onboarding_tutorial = speedyBot(channel)

    # Get the onboarding message payload
    message = onboarding_tutorial.get_message_payload()

    # Post the onboarding message in Slack
    response = slack_web_client.chat_postMessage(**message)

    # Capture the timestamp of the message we've just posted so
    # we can use it to update the message after a user
    # has completed an onboarding task.
    onboarding_tutorial.timestamp = response["ts"]

    # Store the message sent in onboarding_tutorials_sent
    if channel not in onboarding_tutorials_sent:
        onboarding_tutorials_sent[channel] = {}
    onboarding_tutorials_sent[channel][user_id] = onboarding_tutorial
@slack_events_adapter.on("message")
def message(payload):
    """Display the onboarding welcome message after receiving a message
    that contains "start".
    """
    event = payload.get("event", {})

    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")


    if text and text.lower() == "hello":
        return start_onboarding(user_id, channel_id)

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    slack_events_adapter.start(port=3000)

