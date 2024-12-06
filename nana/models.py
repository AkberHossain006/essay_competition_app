from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Competition(models.Model):
    name = models.CharField(max_length=250)
    deadline = models.DateTimeField()

    def __str__(self):
        return f"Name: {self.name} | Deadline date: {self.deadline}"


class EssayTopic(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    def __str__(self):
        return f"Name: {self.name}"


class Essay(models.Model):
    content = models.TextField()
    essay_topic = models.ForeignKey(EssayTopic, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"Essay Content: {self.content[:10]}"