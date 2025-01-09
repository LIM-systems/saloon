# Generated by Django 4.2.7 on 2024-03-14 10:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inwork', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Broadcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название рассылки')),
                ('text', models.TextField(help_text='В тексте можно использовать HTML теги и вставлять имя клиента {name}', verbose_name='Текст сообщения')),
                ('photo', models.CharField(blank=True, help_text='Ссылка на фото, не обязательный параметр', max_length=255, null=True, verbose_name='Фото')),
                ('video', models.CharField(blank=True, help_text='Ссылка на видео, не обязательный параметр', max_length=3000, null=True, verbose_name='Видео')),
                ('send_datetime', models.DateTimeField(help_text='Указывайте московское время отправки', verbose_name='Когда отправить')),
                ('filename', models.CharField(help_text='Имя файла csv с выборкой клиентов', max_length=255, verbose_name='Имя файла')),
            ],
            options={
                'verbose_name': 'Ручные рассылки',
                'verbose_name_plural': 'Ручные рассылки',
                'ordering': ('-send_datetime',),
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категорию',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=12)),
            ],
            options={
                'verbose_name': 'Персона',
                'verbose_name_plural': 'Персона',
            },
        ),
        migrations.RemoveField(
            model_name='masterscheduletime',
            name='master_schedule',
        ),
        migrations.AlterModelOptions(
            name='visitjournal',
            options={'verbose_name': 'Журнал посещений', 'verbose_name_plural': 'Журнал посещений'},
        ),
        migrations.RenameField(
            model_name='client',
            old_name='telegram_id',
            new_name='tg_id',
        ),
        migrations.RemoveField(
            model_name='master',
            name='servises',
        ),
        migrations.RemoveField(
            model_name='master',
            name='telegram_id',
        ),
        migrations.AddField(
            model_name='client',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='client',
            name='gender',
            field=models.CharField(blank=True, choices=[('m', 'Мужчина'), ('w', 'Женщина')], max_length=255, null=True, verbose_name='Пол'),
        ),
        migrations.AddField(
            model_name='client',
            name='is_blocked',
            field=models.BooleanField(blank=True, null=True, verbose_name='Бот заблокирован'),
        ),
        migrations.AddField(
            model_name='client',
            name='last_visit',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Последнее посещение'),
        ),
        migrations.AddField(
            model_name='master',
            name='photo',
            field=models.ImageField(default=1, upload_to='masters/', verbose_name='Фото мастера'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='master',
            name='services',
            field=models.ManyToManyField(blank=True, to='inwork.service', verbose_name='Услуги'),
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='services/', verbose_name='Картинка услуги'),
        ),
        migrations.AddField(
            model_name='visitjournal',
            name='cancel',
            field=models.BooleanField(default=False, verbose_name='Услуга отменена'),
        ),
        migrations.AddField(
            model_name='visitjournal',
            name='confirmation',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Подтверждение'),
        ),
        migrations.AddField(
            model_name='visitjournal',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='visitjournal',
            name='estimation',
            field=models.IntegerField(blank=True, null=True, verbose_name='Оценка'),
        ),
        migrations.AddField(
            model_name='visitjournal',
            name='finish',
            field=models.BooleanField(default=False, verbose_name='Услуга оказана'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(help_text='Введите ФИО клиента', max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(default='+7', help_text='Введите телефон в формате +79001112233', max_length=12, validators=[django.core.validators.RegexValidator(message='Номер должен быть в формате +79001112233', regex='^\\+7\\d{10}$')], verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='master',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inwork.client', verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='master',
            name='rate',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='masterschedule',
            name='end_time',
            field=models.TimeField(default='21:00:00', verbose_name='Конец работы'),
        ),
        migrations.AlterField(
            model_name='masterschedule',
            name='start_time',
            field=models.TimeField(default='10:00:00', verbose_name='Начало работы'),
        ),
        migrations.RemoveField(
            model_name='service',
            name='categories',
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='service',
            name='duration',
            field=models.IntegerField(verbose_name='Длительность выполнения (минут)'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.IntegerField(verbose_name='Цена(рублей)'),
        ),
        migrations.AlterField(
            model_name='visitjournal',
            name='date',
            field=models.DateTimeField(verbose_name='Дата посещения'),
        ),
        migrations.AlterField(
            model_name='visitjournal',
            name='visit_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inwork.service', verbose_name='Услуга'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='MasterScheduleTime',
        ),
        migrations.AddField(
            model_name='service',
            name='persons',
            field=models.ManyToManyField(help_text='Выберите для кого доступна услуга', to='inwork.person', verbose_name='Персоны'),
        ),
        migrations.AddField(
            model_name='service',
            name='categories',
            field=models.ManyToManyField(to='inwork.categories', verbose_name='Категории'),
        ),
    ]