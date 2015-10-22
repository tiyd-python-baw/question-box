from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=1000, null=True, blank=True)
    timestamp = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User)
    points_q = models.IntegerField(default=0)

class Answers(models.Model):
    text = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(default=datetime.now())
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)
    points_a =models.IntegerField(default=0)

class Score(models.Model):
    points = models.IntegerField(default=0)
    user = models.OneToOneField(User)