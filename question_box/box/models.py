from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=1000, null=True, blank=True)
    timestamp = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User)
    tags = models.ManyToManyField('Tag', related_name='questions')
class Answers(models.Model):
    text = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(default=datetime.now())
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)
    voter = models.ForeignKey(User, null = True, related_name='voter')
    points_a =models.IntegerField(default=0)

class Score(models.Model):
    points = models.IntegerField(default=0)
    user = models.OneToOneField(User)

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
