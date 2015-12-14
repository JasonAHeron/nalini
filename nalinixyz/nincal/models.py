from django.db import models

# Create your models here.

class Day(models.Model):
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class Event(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

    def __str__(self):
        return "D {} | C {}".format(self.day, self.content)


class Poll(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.IntegerField(default=0)

    def __str__(self):
        return "D {} | N {} | V {}".format(self.day, self.name, self.value)
