from django.db import models
import datetime
from django.utils import timezone


class Stock(models.Model):
    company = models.CharField(max_length=100)
    ticker = models.CharField(max_length=6)
    timestamp = models.DateTimeField('timestamp')

    def was_saved_recently(self):
        return self.timestamp >= timezone.now() - datetime.timedelta(days=3)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.company