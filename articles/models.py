from django.db import models
import datetime
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField()

    def __unicode__(self):
        return self.title