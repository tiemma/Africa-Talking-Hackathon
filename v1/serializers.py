from rest_framework import serializers

from .models import Topic,  Task, Article

class TagListSerializer(serializers.Field):
    def to_internal_value(self, data):
        if type(data) is not list:
            raise ParseError("expected a list of data")
        return data

    def to_representation(self, obj):
        if type(obj) is not list:
            return [tag.name for tag in obj.all()]
        return obj
    
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
    
    articles = ArticleSerializer(many=True)
    tasks = TaskSerializer(many=True)
    
    class Meta:
        model = Topic
        fields = ('pk', 'name', 'description', 'articles', 'tags', 'tasks')
        depth = 1
        read_only_fields = ('pk', )
