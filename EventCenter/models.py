from django.conf import settings
from django.db import models
from django.db.models.functions import datetime


class Channel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'channel_tab'


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    timestamp = models.IntegerField()
    location = models.CharField(max_length=200)
    image_url = models.URLField()

    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def date(self):
        d = datetime.datetime.fromtimestamp(self.timestamp)
        return d

    class Meta:
        db_table = 'event_tab'


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'comment_tab'


class Participation(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + ' participate in ' + self.event.title

    class Meta:
        db_table = 'participation_tab'


class Like(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + ' likes ' + self.event.title

    class Meta:
        db_table = 'like_tab'
