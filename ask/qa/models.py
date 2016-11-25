from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.

class QuestionManager(models.Manager):

    def new(self):
        qs = super(QuestionManager, self).get_queryset()
        return qs.order_by('-id')

    def popular(self):
        qs = super(QuestionManager, self).get_queryset()
        return qs.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name="question_author")
    likes = models.ManyToManyField(User)

    def get_url(self):
        return '/question/{}/'.format(self.id)

    def __unicode__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, related_name="answer_author")

    def __unicode__(self):
        return self.text
