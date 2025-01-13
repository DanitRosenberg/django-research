
# Create your models here.

from django.db import models

class Guest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    QUESTION_TYPES = (
        ('text', 'טקסט חופשי'),
        ('multiple_choice', 'בחירה מרובה'),
    )
    text = models.TextField()
    question_type = models.CharField(max_length=50, choices=QUESTION_TYPES, default='text')
    options = models.TextField(blank=True, null=True, help_text='הפרידי בין האפשרויות באמצעות פסיק')

    def __str__(self):
        return self.text

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.question.text}"





AUTH_USER_MODEL = 'your_app.CustomUser'

