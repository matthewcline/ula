from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=200)
    integration_id = models.CharField(max_length=200)

class Task(models.Model):
    text = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    emoji = models.CharField(max_length=100)

class UserTask(models.Model):
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    date_completed = models.DateField(null=True)

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
