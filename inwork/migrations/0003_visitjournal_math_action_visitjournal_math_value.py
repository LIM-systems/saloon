# Generated by Django 4.2.7 on 2024-03-21 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inwork', '0002_broadcast_categories_person_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitjournal',
            name='math_action',
            field=models.CharField(choices=[('plus', 'Прибавить'), ('minus', 'Вычесть')], default='plus', max_length=255, verbose_name='Действие'),
        ),
        migrations.AddField(
            model_name='visitjournal',
            name='math_value',
            field=models.IntegerField(default=0, verbose_name='Значение'),
        ),
    ]
