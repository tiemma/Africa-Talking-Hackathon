from django.db import models
from taggit.managers import TaggableManager

class Topic(models.Model):
    name = models.CharField(max_length=150, blank=True)
    description = models.TextField()
    tags = TaggableManager()

    def __str__(self):
        return self.name

class Task(models.Model):
    topic = models.ForeignKey(Topic, related_name="tasks", null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Task for {self.topic}"

class Article(models.Model):
    topic = models.ForeignKey(Topic, related_name="articles", null=True)
    url = models.URLField(blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return f'{self.url} for {self.topic}'
