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

    @property
    def options(self):
        op = Option.objects.filter(poll=self)
        return ", ".join([o.name for o in op])

    def __str__(self):
        return "D {} | N {} | O {}".format(self.day, self.name, self.options)

class Option(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    @property
    def value(self):
        return len(Vote.objects.filter(option=self))

    def __str__(self):
        return "P {} | N {} | V {}".format(self.poll.name, self.name, self.value)

class Vote(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    time = models.CharField(max_length=100)

    @property
    def name(self):
        return self.option.name

    def __str__(self):
        return "O {} | T {}".format(self.option, self.time)
