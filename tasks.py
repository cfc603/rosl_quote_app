from dj_tasks.tasks import Task

from .models import Quote


class SendQuoteTask(Task):

    name = "Send Quote"
    frequency = 60

    def run(self):
        Quote.send_quotes()
