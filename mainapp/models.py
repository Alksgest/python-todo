from django.db import models


class TodoModel(models.Model):
    title = models.CharField(verbose_name='Title', max_length=20, default='Default Title')
    date = models.DateField(verbose_name='Date')
    content = models.TextField(verbose_name='Content')
    owner = models.ForeignKey('auth.User', related_name='todos', default=1, on_delete=models.CASCADE)
