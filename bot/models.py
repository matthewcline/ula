from django.db import models


class Task(models.Model):
    text = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    emoji = models.CharField(max_length=100)

# User
# - username
# - slack user id (used for channel)
#
# UserTask (many to many)
# - user
# - task
# - completed
# - date
#
# Message
# - text
# - timestamp
# - channel
#
# Challenge:
# - initial (Message)
# - check in intro (Message)
# - channel message indicating someone completed something (Message)
# - array of Tasks
# - frequency
# - duration
#
# UserChallenge:
# - Challenge
# - User
# - date started
# - completed
