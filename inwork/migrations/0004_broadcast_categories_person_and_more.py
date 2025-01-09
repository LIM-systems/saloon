# Generated by Django 4.2.7 on 2024-08-14 16:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inwork', '0003_broadcast_categories_person_shoppingjournal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingjournal',
            name='client',
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to='inwork.client', verbose_name='Клиент'),
            preserve_default=False,
        ),
    ]
