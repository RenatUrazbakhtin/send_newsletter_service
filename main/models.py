from django.db import models

from config import settings

# Create your models here.
NULLABLE = {'null': True, 'blank': True}
class Client(models.Model):
    email = models.EmailField(max_length=100, verbose_name='Почта')
    first_name = models.CharField(max_length=100, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', **NULLABLE)
    comment = models.TextField(max_length=1000, verbose_name='Комментарий')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name = 'создатель рассылки', ** NULLABLE)
    def __srt__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

