import json
from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from comments.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post_id', 'post', 'comment')
    list_filter = ('user', 'post_id')

    def changelist_view(self, request, extra_context=None):
        chart_data = self.chart_data()
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)

        user_comments = Comment.objects.values("user__username") \
            .annotate(y=Count("id")) \
            .order_by("-user__username")
        user_comments_json = json.dumps(list(user_comments), cls=DjangoJSONEncoder)

        extra_context = extra_context or \
            {"chart_data": as_json, "user_comments": user_comments_json}

        return super().changelist_view(request, extra_context=extra_context)

    def chart_data(self):
        return (
            Comment.objects
                .values("post__title")
                .annotate(y=Count("id"))
                .order_by("-post")
        )
