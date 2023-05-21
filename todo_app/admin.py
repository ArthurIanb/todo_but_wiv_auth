from django.contrib import admin
from .models import Task

admin.site.register(Task)   # Register model-task to see it in admin page