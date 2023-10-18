from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'null': True, 'blank': True}
# Create your models here.
class User(AbstractUser):
    """
    Модель пользователя с регистрацией по почте
    """
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    first_name = models.CharField(max_length=50, verbose_name='имя', **NULLABLE)
    last_name = models.CharField(max_length=50, verbose_name='фамилия', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    token = models.CharField(max_length=255, verbose_name='токен верификации', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'