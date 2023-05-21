from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=50, blank=False)    # Title of task
    done = models.BooleanField(default=False)               # Done or not task
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def __repr__(self):
        return str(self)