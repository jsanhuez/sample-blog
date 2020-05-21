from django.contrib import admin
from analytics.models import ObjectViewed

@admin.register(ObjectViewed)
class ObjectViewedAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'content_type', 'viewed_on', 'user', 'ip_address')
