import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models fromhere.
class Tag(models.Model):
  name = models.CharField(max_length=32, unique=True)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ('name',)

class Article(models.Model):
  author = models.ForeignKey(to=User,on_delete=models.CASCADE,)
  title = models.CharField(max_length=128)
  text = models.TextField()
  posted_at = models.DateTimeField(auto_now_add=True)
  last_modify = models.DateTimeField(auto_now=True)
  like = models.IntegerField(default=0)
  tags = models.ManyToManyField(Tag, blank=True)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ('title',)

class Comment(models.Model):
  text = models.TextField()
  posted_at = models.DateTimeField(auto_now_add=True)
  article = models.ForeignKey(to=Article, related_name='comments', on_delete=models.CASCADE)
  def __str__(self):
    return self.text
