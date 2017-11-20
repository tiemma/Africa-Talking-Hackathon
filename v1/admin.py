from django.contrib import admin

from .models import Topic, Task, Article

admin.site.register(Topic)
admin.site.register(Task)
admin.site.register(Article)