"""
Posts URLs.
"""

from django.urls import path
from django.conf import settings
from django.contrib.auth.decorators import login_required

from posts import views

urlpatterns = [
    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='blog'
    ),
    path(
        route='posts/<slug:url>/',
        view=login_required(views.PostDetailView.as_view()),
        name='detail'
    ),
    path(
        route='posts/save_comment',
        view=views.save_comment,
        name='save_comment'
    ),
]
