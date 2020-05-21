import json
from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from analytics.models import ObjectViewed

@admin.register(ObjectViewed)
class ObjectViewedAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'content_type', 'viewed_on', 'user', 'ip_address')

    def changelist_view(self, request, extra_context=None):
        # Aggregate number of post visited per user
        user_num_post = ObjectViewed.objects \
            .values("user__username") \
            .annotate(y=Count("object_id")) \
            .order_by("user__username")
        as_json = json.dumps(list(user_num_post), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"user_num_post": as_json}

        return super().changelist_view(request, extra_context=extra_context)