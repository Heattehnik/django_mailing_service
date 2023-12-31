# Generated by Django 4.2.3 on 2023-07-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('content', models.TextField(verbose_name='содержимое статьи')),
                ('image', models.ImageField(upload_to='images/', verbose_name='изображение')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='просмотры')),
                ('published_at', models.DateField(verbose_name='дата публикации')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
            },
        ),
    ]
