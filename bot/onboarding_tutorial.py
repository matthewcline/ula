TASKS = [
    {
        'text': 'Read 10 pages a day',
        'emoji': ':nerd_face:'
    },
    {
        'text': 'Workout at least 45 mins',
        'emoji': ':muscle:'
    },
    {
        'text': 'Drink a gallon of water',
        'emoji': ':droplet:'
    }
]


# class Message:
#     def __init__(self, channel):
#         self.channel = channel
#         self.username = "pythonboardingbot"
#         self.icon_emoji = ":robot_face:"
#         self.timestamp = ""


class Task:
    def __init__(self, text, emoji):
        self.text = text
        self.emoji = emoji
        self.completed = False

    def get_text(self):
        return self.text

    def get_emoji(self):
        return self.emoji


# TODO: inherit from Message
class TaskMessage:
    """Constructs the tasks message and stores the state of which tasks were completed."""

    def __init__(self, channel, intro_text):
        self.channel = channel
        self.username = "pythonboardingbot"
        self.icon_emoji = ":robot_face:"
        self.timestamp = ""

        self.intro_text = intro_text
        self.tasks = [Task(task.get('text'), task.get('emoji')) for task in TASKS]

    DIVIDER_BLOCK = {"type": "divider"}

    def get_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self._get_welcome_block(),
                self.DIVIDER_BLOCK,
                *self._get_task_blocks()
            ],
        }

    def _get_welcome_block(self):
        return {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": self.intro_text
            },
        }

    def _get_task_blocks(self):
        return [self._get_task_block(task) for task in self.tasks]

    def _get_task_block(self, task: Task):
        text = (
            f"{self._get_task_checkmark(task)} {task.get_text()}"
        )
        task_block = {"type": "section", "text": {"type": "mrkdwn", "text": text}}
        return task_block

    @staticmethod
    def _get_task_checkmark(task: Task) -> str:
        if task.completed:
            return task.emoji
        return ":white_large_square:"

    # @staticmethod
    # def _get_task_block(text, information):
    #     return [
    #         {"type": "section", "text": {"type": "mrkdwn", "text": text}},
    #         {"type": "context", "elements": [{"type": "mrkdwn", "text": information}]},
    #     ]
