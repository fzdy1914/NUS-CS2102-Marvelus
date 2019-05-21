from django.contrib import admin
from EventCenter.models import Event, Channel, Comment


class EventAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'timestamp', 'location', 'image_url', 'channel']
    list_display = ['id', 'title', 'date', 'channel']
    list_filter = ['channel']
    search_fields = ['title']


class ChannelAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['id', 'name']
    search_fields = ['name']


class CommentAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'user', 'event']
    list_display = ['id', 'event_id', 'title', 'user']
    list_filter = ['event']


admin.site.register(Event, EventAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(Comment, CommentAdmin)

admin.AdminSite.site_header = 'Event Center Management'
