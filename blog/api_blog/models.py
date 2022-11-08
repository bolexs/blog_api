from django.db import models
from datetime import datetime

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    

    def __str__(self):
        return f'{self.first_name}'


class Post(models.Model):
    author_id = models.ForeignKey(Author, null=True, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, null=True)

    def __str__(self):
        return f'{self.title} by {self.author_id}'