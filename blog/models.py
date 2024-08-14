import datetime
from django.db import models
from pathlib import Path


# Create your models here.
class Author(models.Model):
    username = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username
    

class Post(models.Model):
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='posts', null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='post', null=True)
    date = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=255, default='No Title', db_index=True)
    excerpt = models.TextField(default='No excerpt provided.')
    content = models.TextField(default='No content provided.')

    objects = models.Manager()
    
    def get_absolute_url(self):
        return reverse('post-detail-page', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title

   
    

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='comment', null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content
    