import logging
import random
from slack_bolt import App
from slack_sdk.web import WebClient
from onboarding_tutorial import TaskMessage

app = App()

onboarding_tutorials_sent = {}

# An idea for a challenge is to go to the gym at least 3 times a week
# provide updates 2 times a week (Wednesday and Friday) to avoid overloading

greeting_messages = ["What's up", "Howdy", "Yello", "How's it going,"]

check_in = "Hi Matt, did you accomplish your goal today?  Please respond with a {:strong:} if you did " \
           "and leave a comment with how things are going!"

"Your teammates would love to hear about any accomplishments or challenged you're facing"
"Feel free to pose a question to your teammates"



status_message = "Hi everyone, happy Wednesday!  Here's some comments from your teammates: "

def generate_task_message():
    # use this function to communicate the user's challenge to them

def generate_check_in_message():
    greeting = f"{random.choice(greeting_messages)} {name}!"
    return f"{greeting}"

def start_onboarding(user_id: str, channel: str, client: WebClient):
    # Create a new onboarding tutorial.

    print("starting")

    onboarding_tutorial = TaskMessage(channel, "Welcome back Matt!  Which of these did you crush today?")

    # Get the onboarding message payload
    message = onboarding_tutorial.get_message_payload()

    # Post the onboarding message in Slack
    response = client.chat_postMessage(**message)

    # Capture the timestamp of the message we've just posted so
    # we can use it to update the message after a user
    # has completed an onboarding task.
    onboarding_tutorial.timestamp = response["ts"]

    # Store the message sent in onboarding_tutorials_sent
    if channel not in onboarding_tutorials_sent:
        onboarding_tutorials_sent[channel] = {}
    onboarding_tutorials_sent[channel][user_id] = onboarding_tutorial

# ================ Team Join Event =============== #
# When the user first joins a team, the type of the event will be 'team_join'.
# Here we'll link the onboarding_message callback to the 'team_join' event.

# Note: Bolt provides a WebClient instance as an argument to the listener function
# we've defined here, which we then use to access Slack Web API methods like conversations_open.
# For more info, checkout: https://slack.dev/bolt-python/concepts#message-listening
@app.event("team_join")
def onboarding_message(event, client):
    """Create and send an onboarding welcome message to new users. Save the
    time stamp of this message so we can update this message in the future.
    """
    # Get the id of the Slack user associated with the incoming event
    user_id = event.get("user", {}).get("id")

    # Open a DM with the new user.
    response = client.conversations_open(users=user_id)
    channel = response["channel"]["id"]

    # Post the onboarding message.
    start_onboarding(user_id, channel, client)


# ============= Reaction Added Events ============= #
# When a users adds an emoji reaction to the onboarding message,
# the type of the event will be 'reaction_added'.
# Here we'll link the update_emoji callback to the 'reaction_added' event.
@app.event("reaction_added")
def update_emoji(event, client):
    """Update the onboarding welcome message after receiving a "reaction_added"
    event from Slack. Update timestamp for welcome message as well.
    """
    # Get the ids of the Slack user and channel associated with the incoming event
    channel_id = event.get("item", {}).get("channel")
    user_id = event.get("user")

    emoji = event.get("reaction")

    if channel_id not in onboarding_tutorials_sent:
        return

    # Get the original tutorial sent.
    onboarding_tutorial = onboarding_tutorials_sent[channel_id][user_id]

    for task in onboarding_tutorial.tasks:
        if task.emoji == f':{emoji}:':
            task.completed = True

    # Get the new message payload
    message = onboarding_tutorial.get_message_payload()

    # Post the updated message in Slack
    updated_message = client.chat_update(**message)

# ============== Message Events ============= #
# When a user sends a DM, the event type will be 'message'.
# Here we'll link the message callback to the 'message' event.
@app.event("message")
def message(event, client):
    """Display the onboarding welcome message after receiving a message
    that contains "start".
    """
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")

    if text and text.lower() == "start":
        return start_onboarding(user_id, channel_id, client)


# ============== Channel Events ============= #

@app.event("channel_joined")
def handle_channel_joined():
    pass

@app.event("channel_left")
def handle_channel_left():
    # opt the user out of the challenge
    pass


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    app.start(3000)

import ssl as ssl_lib
import certifi

ssl_context = ssl_lib.create_default_context(cafile=certifi.where())

