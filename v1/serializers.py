from rest_framework import serializers

from .models import Topic, Stage, Task, Article

class TaskSerializer(serializers.Serializer):

    class Meta:
        model = Task
        fields = '__all__'

class ArticleSerializer(serializers.Serializer):

    class Meta:
        model = Article
        fields = '__all__'

class StageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stage
        fields = '__all__'

class BasicTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('pk', 'name', 'description', 'tags', 'articles', 'tasks')
        read_only_fields = ('pk', )
        extra_kwargs = { "articles" : {"write_only" : True}, "tasks" : {"write_only" : True} }

class TopicSerializer(serializers.ModelSerializer):
    
    # stages = StageSerializer(many=True)
    
    class Meta:
        model = Topic
        fields = ('pk', 'name', 'description', 'articles', 'tags', 'tasks')
        # fields = '__all__'
        read_only_fields = ('pk', )
