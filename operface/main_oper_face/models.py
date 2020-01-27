from django.db import models
from django.utils import timezone



class Instalator(models.Model):
    chat_id = models.IntegerField()
    name = models.CharField(max_length=200)
    score = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Installation(models.Model):
    #id = models.AutoField()
    Instalator_id = models.ForeignKey('Instalator',on_delete = models.DO_NOTHING)
    location = models.CharField(max_length=200)
    date = models.DateTimeField()
    #time = models.TimeField()
    answer = models.TextField()
    #photo = models.FilePathField()

    def __str__(self):
        return self.location
