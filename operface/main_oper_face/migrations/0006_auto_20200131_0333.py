# Generated by Django 3.0.2 on 2020-01-31 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_oper_face', '0005_auto_20200131_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installation',
            name='photo_1',
            field=models.ImageField(upload_to='main_oper_face/static', verbose_name='Фото ОКР'),
        ),
    ]
