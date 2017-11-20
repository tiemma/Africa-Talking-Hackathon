from rest_framework import serializers

from .models import Topic,  Task, Article

class TaskSerializer(serializers.Serializer):

    class Meta:
        model = Task
        fields = ('description')

class ArticleSerializer(serializers.Serializer):

    class Meta:
        model = Article
        fields = ('url', 'text')


class BasicTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('pk', 'name', 'description', 'tags', 'articles', 'tasks')
        read_only_fields = ('pk', )
        extra_kwargs = { "articles" : {"write_only" : True}, "tasks" : {"write_only" : True} }        

class TopicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Topic
        fields = ('pk', 'name', 'description', 'articles', 'tags', 'tasks')
        depth = 1
        read_only_fields = ('pk', )
