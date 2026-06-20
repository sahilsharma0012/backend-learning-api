from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    title = models.CharField(max_length = 100)
    completed = models.BooleanField(default = False)
    
    document = models.FileField(upload_to = 'documents/', null = True, blank = True)
    
    def __str__(self):
        return self.title