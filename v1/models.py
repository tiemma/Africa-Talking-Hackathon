from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=150, blank=True)
    description = models.TextField()
    tags = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Stage(models.Model):
    name = models.CharField(max_length=150, blank=True)    
    topic = models.ForeignKey('Topic', related_name="stages")

    def __str__(self):
        return f"{self.name} for {self.topic}"

class Task(models.Model):
    # stage = models.ForeignKey('Stage', related_name='topics', null=True)
    topic = models.ForeignKey('Topic', related_name="tasks", null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Task for {self.topic}"

class Article(models.Model):
    # stage = models.ForeignKey('Stage', related_name='articles', null=True)
    topic = models.ForeignKey('Topic', related_name="articles", null=True)
    url = models.URLField(blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return f'{self.url} for {self.topic}'
