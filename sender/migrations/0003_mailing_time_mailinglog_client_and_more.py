# Generated by Django 4.2.3 on 2023-07-24 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sender', '0002_alter_client_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='time',
            field=models.CharField(choices=[('09:00', '09:00'), ('12:00', '12:00'), ('15:00', '15:00'), ('18:00', '18:00')], default='09:00', max_length=5, verbose_name='время рассылки'),
        ),
        migrations.AddField(
            model_name='mailinglog',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sender.client', verbose_name='клиент'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='send_period',
            field=models.CharField(choices=[('daily', 'Раз в день'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], default='daily', max_length=7, verbose_name='периодичность'),
        ),
    ]