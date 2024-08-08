from django.db import models
from pathlib import Path


# Create your models here.
class Author(models.Model):
    username = models.CharField(max_length=255)
   
    def __str__(self):
        return self.username
    

class Post(models.Model):
    slug = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=255)
    excerpt = models.TextField()
    content = models.TextField()
    
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    