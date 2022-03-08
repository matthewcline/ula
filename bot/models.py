from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=200)
    integration_id = models.CharField(max_length=200)

class Task(models.Model):
    text = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    emoji = models.CharField(max_length=100)
    challenge = models.ForeignKey('Challenge', on_delete=models.CASCADE)

class UserTask(models.Model):
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    date_completed = models.DateField(null=True)

class Message(models.Model):
    text = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class Challenge(models.Model):
    welcome_msg = models.ForeignKey('Message', on_delete=models.CASCADE)
    check_in_msg = models.ForeignKey('ScheduledMessage', on_delete=models.CASCADE)
    team_status_message = models.ForeignKey('ScheduledMessage', on_delete=models.CASCADE)
    team_stats_message = models.ForeignKey('ScheduledMessage', on_delete=models.CASCADE)

# UserChallenge:
# - Challenge
# - User
# - date started
# - completed

# ScheduledMessage (Message):
# - type (check in, status, stats)
# - text
# - challenge
# - time during the day to send message
# - frequency of message (options are daily, every 2 days, weekly, every 2 weeks, monthly)

# Log
# - text
# - timestamp
# - channel