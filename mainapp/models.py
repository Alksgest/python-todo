from django.db import models
from django.urls import reverse

class TodoModel(models.Model):
    date = models.DateField(verbose_name="Date")
    content = models.TextField(verbose_name='Content')

