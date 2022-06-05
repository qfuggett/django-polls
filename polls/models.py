import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  #Django supports all common database relationships
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

"""
Making Model Changes

Change your models (in models.py).
Run python manage.py makemigrations to create migrations for those changes
python manage.py sqlmigrate polls 0001 [optional; sees what sql thinks is required]
Run python manage.py migrate to apply those changes to the database.

"""