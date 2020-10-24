from slack import WebClient
from speedy import speedyBot
import os

# Create a slack client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Get a new NestorBot
speedy_bot = SpeedyBot("#creación-de-bot")

# Get the onboarding message payload
message = speedy_bot.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**message)
