from django.db import models
import datetime
from django.utils import timezone

class Location(models.Model):
    location = models.CharField(max_length=200)
    timestamp = models.DateTimeField('timestamp')

    def was_saved_recently(self):
        return self.timestamp >= timezone.now() - datetime.timedelta(days=3)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.location


class Tweets(models.Model):
    location = models.ForeignKey(Location)
    tweet_text = models.CharField(max_length=140)
    number = models.IntegerField(default=0)