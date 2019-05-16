from django.contrib import admin
from EventCenter.models import Event, Channel, Comment


class EventAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'timestamp', 'location', 'image_url', 'channel']
    list_display = ('title', 'date', 'channel')
    list_filter = ["channel"]
    search_fields = ['title']


admin.site.register(Event, EventAdmin)
admin.site.register(Channel)
admin.site.register(Comment)
