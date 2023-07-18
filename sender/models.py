from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=50, verbose_name='фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='отчество')

    email = models.EmailField(max_length=150, verbose_name='почта')
    comment = models.TextField(verbose_name='комментарий')

    def __str__(self):
        return f'{self.first_name} ({self.email})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Mailing(models.Model):
    SEND_PERIOD_CHOICES = (
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    )
    SEND_STATUS_CHOICES = (
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    )
    send_time = models.TimeField(verbose_name='время рассылки')
    send_period = models.CharField(max_length=7, choices=SEND_PERIOD_CHOICES, verbose_name='периодичность')
    send_status = models.CharField(max_length=9, choices=SEND_STATUS_CHOICES, verbose_name='статус')

    def __str__(self):
        return f'{self.send_time} - {self.send_period} - {self.send_status}'

    class Meta:
        verbose_name = 'настройка'
        verbose_name_plural = 'настройки'


class MailingMessage(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='настройка')
    subject = models.CharField(max_length=255, verbose_name='тема')
    body = models.TextField(verbose_name='текст письма')

    def __str__(self):
        return f'{self.subject}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class MailingLog(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='настройка')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='дата пследней рассылки')
    status = models.CharField(max_length=255, verbose_name='статус')
    response = models.TextField(blank=True, null=True, verbose_name='ответ сервера')

    def __str__(self):
        return f'{self.timestamp} - {self.status}'

    class Meta:
        verbose_name = 'попытка'
        verbose_name_plural = 'попытки'