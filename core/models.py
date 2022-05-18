from django.db import models

# Create your models here.


class Task(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    desc = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title