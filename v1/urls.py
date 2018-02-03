from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

from .views import index, TopicView, TopicDetailView, ArticleDetailView, TaskDetailView

urlpatterns = [    
    url(r'^topics/$', TopicView.as_view()),
    url(r'^topics/(?P<pk>[0-9]+)/$', TopicDetailView.as_view()),
    url(r'^articles/(?P<pk>[0-9]+)/$', ArticleDetailView.as_view()),
    url(r'^tasks/(?P<pk>[0-9]+)/$', TaskDetailView.as_view()),
]
