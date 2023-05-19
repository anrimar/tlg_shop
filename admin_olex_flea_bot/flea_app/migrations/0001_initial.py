# Generated by Django 3.1.1 on 2020-09-14 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.PositiveIntegerField(unique=True, verbose_name='ID пользователя в Telegram')),
                ('username', models.TextField(verbose_name='Ник в Telegram')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Администратор')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.PositiveIntegerField(verbose_name='ID сообщения в Барахолке')),
                ('type_p', models.TextField(verbose_name='Тип поста')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время получения')),
                ('reviewed_at', models.DateTimeField(verbose_name='Время рассмотрения')),
                ('status', models.CharField(choices=[('1', 'На рассмотрении'), ('2', 'Подтверждено'), ('3', 'Отклонено'), ('4', 'Ожидает оплаты'), ('5', 'Продано'), ('6', 'Создается')], default='1', max_length=20, verbose_name='Статус')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flea_app.profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
