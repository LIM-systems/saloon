# Generated by Django 4.2.7 on 2024-03-22 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inwork', '0005_alter_visitjournal_math_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitjournal',
            name='math_action',
            field=models.CharField(choices=[('plus', 'Прибавление'), ('minus', 'Вычитание')], default='plus', max_length=255, verbose_name='Действие'),
        ),
    ]
