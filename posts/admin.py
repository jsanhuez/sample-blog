import json
from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'image_header', 'created', 'modified', 'is_draft')
    search_fields = ('title', 'user__username', 'user__email')
    list_filter = ('created', 'modified')
    actions = ('set_posts_to_published', )

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ('url', )
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user
        form.base_fields['profile'].initial = request.user.profile
        return form

    def set_posts_to_published(self, request, queryset):
        count = queryset.update(is_draft=False)
        self.message_user(request, '{} posts have been published successfully'.format(count))

    def changelist_view(self, request, extra_context=None):
        # Aggregate new post per day
        chart_data = self.chart_data()
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        return super().changelist_view(request, extra_context=extra_context)

    def chart_data(self):
        return (
            Post.objects.annotate(date=TruncDay("modified"))
                .values("date")
                .annotate(y=Count("id"))
                .order_by("-date")
        )
