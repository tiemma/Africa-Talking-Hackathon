from django.shortcuts import HttpResponse

from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Topic, Task, Article
from .serializers import BasicTopicSerializer, TopicSerializer, ArticleSerializer, TaskSerializer

def index(request):
    return HttpResponse(content=b'Hello world')

class TopicView(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = BasicTopicSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'tags')

class TopicDetailView(generics.RetrieveUpdateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class ArticleDetailView(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class TaskDetailView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer