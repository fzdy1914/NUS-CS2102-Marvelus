from rest_framework import serializers
from .models import Event


class DetailEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'timestamp', 'location', 'image_url', 'channel')


class BriefEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'timestamp', 'channel')
