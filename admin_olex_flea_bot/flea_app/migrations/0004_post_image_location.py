# Generated by Django 3.1.1 on 2020-09-14 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flea_app', '0003_auto_20200914_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_location',
            field=models.TextField(null=True, verbose_name='Расположение фото'),
        ),
    ]
