from django.conf import settings
from django.db import models
from django.db.models.functions import datetime


class Channel(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'channel_tab'


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    timestamp = models.IntegerField()
    location = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)

    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

    idx_date = models.Index(fields=['date'])
    idx_channel_id = models.Index(fields=['channel_id'])

    def __str__(self):
        return self.title

    def date(self):
        d = datetime.datetime.fromtimestamp(self.timestamp)
        return d

    class Meta:
        db_table = 'event_tab'


class Comment(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    idx_event_id = models.Index(fields=['event_id'])

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'comment_tab'


class Participation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + ' participate in ' + self.event.title

    class Meta:
        db_table = 'participation_tab'


class Like(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + ' likes ' + self.event.title

    class Meta:
        db_table = 'like_tab'
