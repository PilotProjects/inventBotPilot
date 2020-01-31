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
    photo_1 = models.ImageField('Выполнена ли проводка кабеля в подъезде?' , upload_to='main_oper_face/static')
    photo_2 = models.ImageField('Необходимо ли проделать доп. отверстие для ввода кабеля в жилое помещение?' , upload_to='main_oper_face/static')
    photo_3 = models.ImageField('Необходимо ли проделать доп отверстие в помещении?' , upload_to='main_oper_face/static')
    photo_4 = models.ImageField('Логин и пароль от Wi-Fi сети наклеен на оборудование?' , upload_to='main_oper_face/static')
    photo_5 = models.ImageField('Продемонстрирована скорость подключения?' , upload_to='main_oper_face/static')
    


    def __str__(self):
        return self.location
