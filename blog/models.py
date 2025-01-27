from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
class Post(models.Model):

    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = 'PB','Published'

    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length = 250)
    body = models.TextField()
    publish = models.DateTimeField(default =timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length = 2,choices=Status.choices,default=Status.Draft)
    class Meta:
        ordering = ['-publish']
    def __str__(self):
        return self.title
    