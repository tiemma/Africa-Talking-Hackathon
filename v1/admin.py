from django.contrib import admin

from .models import Topic, Stage, Task, Article

admin.site.register(Topic)
admin.site.register(Stage)
admin.site.register(Task)
admin.site.register(Article)