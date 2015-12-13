from django.db import models

# Create your models here.

class Day(models.Model):
    date = models.DateField()


class Event(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    content = models.CharField()
