from django.shortcuts import HttpResponse

from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Topic, Stage, Task, Article
from .serializers import BasicTopicSerializer, TopicSerializer, StageSerializer

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