# Generated by Django 4.2 on 2023-04-22 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='datetime',
            field=models.DateTimeField(default='2023-22-04 12:31:38', verbose_name='Дата публикации'),
        ),
    ]
