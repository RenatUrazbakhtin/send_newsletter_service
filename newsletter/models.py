from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}

class NewsletterMessage(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тема')
    body = models.TextField(max_length=1000, verbose_name='Тело')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сообщение рассылки'
        verbose_name_plural = 'Сообщения рассылок'

class NewsletterSettings(models.Model):
    newsletter_time_from = models.TimeField(auto_now_add=True, verbose_name='Время начала рассылки')
    newsletter_time_to = models.TimeField(auto_now_add=True, verbose_name='Время окончания рассылки')
    periodicity = models.CharField(max_length=100, verbose_name='Периодичность')
    status = models.CharField(max_length=100, default='Создана', verbose_name='Статус')

    newsletter = models.ForeignKey(NewsletterMessage, on_delete=models.CASCADE, verbose_name='Тема')
    def __str__(self):
        return f'{self.newsletter_time_from} по {self.newsletter_time_to}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

class NewsletterLog(models.Model):
    last_attempt_time = models.DateTimeField(auto_now_add=True, verbose_name='Последняя попытка')
    attempt_status = models.BooleanField(default=False, verbose_name='Статус попытки')
    feedback = models.TextField(max_length=1000, verbose_name='Ответ')

    newsletter = models.ForeignKey(NewsletterSettings, on_delete=models.CASCADE, verbose_name='Рассылка')

    def __str__(self):
        return self.feedback

    class Meta:
        verbose_name = 'Лог рассылки'
        verbose_name_plural = 'Логи рассылок'