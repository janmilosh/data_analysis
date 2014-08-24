from django.db import models
import datetime
from django.utils import timezone


class Stocks(models.Model):
    company = models.CharField(max_length=6)
    timestamp = models.DateTimeField('timestamp')

    def was_saved_recently(self):
        return self.timestamp >= timezone.now() - datetime.timedelta(days=3)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.company


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField()

    def __unicode__(self):
        return self.title