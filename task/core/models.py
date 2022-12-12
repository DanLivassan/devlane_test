from django.db import models


class Task(models.Model):
    text = models.TextField(null=False)
    completed = models.BooleanField(default=False)
