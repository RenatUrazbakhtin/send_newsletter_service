from django.db import models
from django.utils.timezone import now

from config import settings
from main.models import Client


# Create your models here.
NULLABLE = {'null': True, 'blank': True}

periodicity = [
    ('OD', 'Раз в день'),
    ('OW', 'Раз в неделю'),
    ('OM', 'Раз в месяц')
]

status_mode = [
    ('CR', 'Создана'),
    ('LD', 'Запущена'),
    ('ED', 'Завершена')
]

class NewsletterSettings(models.Model):
    periodicity = models.CharField(max_length=100, choices=periodicity, verbose_name='Периодичность')
    status = models.CharField(max_length=100, default='Создана', choices=status_mode, verbose_name='Статус')
    task_id = models.CharField(max_length=100, **NULLABLE)
    newsletter_time_from = models.DateTimeField(verbose_name='Время начала рассылки', **NULLABLE)
    newsletter_time_to = models.DateTimeField(verbose_name='Время окончания рассылки', **NULLABLE)
    last_sent_date = models.DateTimeField(verbose_name='отправлено в', **NULLABLE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='создатель рассылки', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='активность')


    client = models.ManyToManyField(Client, verbose_name='Клиент рассылки')
    def __str__(self):
        return f'{self.newsletter_time_from} по {self.newsletter_time_to}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

class NewsletterMessage(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тема')
    body = models.TextField(max_length=1000, verbose_name='Тело')
    newsletter = models.ForeignKey(NewsletterSettings, on_delete=models.CASCADE, **NULLABLE)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сообщение рассылки'
        verbose_name_plural = 'Сообщения рассылок'

class NewsletterLogManager(models.Manager):
    def create_log(self, attempt_status, newsletter, last_attempt_time=now(), feedback='None'):
        log = self.create(last_attempt_time=last_attempt_time, attempt_status=attempt_status, feedback=feedback, newsletter=newsletter)
        return log
class NewsletterLog(models.Model):
    last_attempt_time = models.DateTimeField(auto_now_add=True, verbose_name='Последняя попытка')
    attempt_status = models.CharField(verbose_name='Статус попытки')
    feedback = models.TextField(max_length=1000, verbose_name='Ответ')

    newsletter = models.ForeignKey(NewsletterSettings, on_delete=models.CASCADE, verbose_name='Рассылка')

    objects = NewsletterLogManager()
    def __str__(self):
        return self.feedback

    class Meta:
        verbose_name = 'Лог рассылки'
        verbose_name_plural = 'Логи рассылок'