# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)        

@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)    
    def __str__(self):
        return self.choice_text

@python_2_unicode_compatible
class Spot(models.Model):
    spot_id = models.IntegerField()
    ava = models.BooleanField(default=False)
    time_updated = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return '%s %s %s' % (self.spot_id, self.ava, self.time_updated)

