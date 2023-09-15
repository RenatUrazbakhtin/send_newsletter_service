from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}
class Client(models.Model):
    email = models.EmailField(max_length=100, verbose_name='Почта')
    first_name = models.CharField(max_length=100, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', **NULLABLE)
    comment = models.TextField(max_length=1000, verbose_name='Комментарий')

    def __srt__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class NewsletterSettings(models.Model):
    newsletter_time_from = models.TimeField(auto_now_add=True, verbose_name='Время начала рассылки')
    newsletter_time_to = models.TimeField(auto_now_add=True, verbose_name='Время окончания рассылки')
    periodicity = models.CharField(max_length=100, verbose_name='Периодичность')
    status = models.CharField(max_length=100, default='Создана', verbose_name='Статус')

    def __str__(self):
        return f'{self.newsletter_time_from} по {self.newsletter_time_to}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

class NewsletterMessage(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тема')
    body = models.TextField(max_length=1000, verbose_name='Тело')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сообщение рассылки'
        verbose_name_plural = 'Сообщения рассылок'

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