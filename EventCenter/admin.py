from django.contrib import admin
from EventCenter.models import Event, Channel, Comment


admin.site.register(Event)
admin.site.register(Channel)
admin.site.register(Comment)
