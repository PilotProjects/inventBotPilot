from django.db import models
from django.utils import timezone



class Instalator(models.Model):
    chat_id = models.IntegerField( 'айди инсталлятора' , primary_key=True )
    name = models.CharField( 'ФИО' , max_length=200)
    score = models.PositiveSmallIntegerField('Общий счёт')

    def __str__(self):
        return self.name


class Installation(models.Model):
    #installation_id = models.AutoField('айди инсталляции' , primary_key=True)
    Instalator_id = models.ForeignKey('Instalator' , on_delete = models.DO_NOTHING)
    location = models.CharField('Местоположение', max_length=200)
    date = models.CharField('Время' , max_length=200)
    #time = models.TimeField()
    answer = models.TextField('Ответы на вопросы')
    #photo = models.FilePathField()

    def __str__(self):
        return self.location
