from django.db import models

NULLABLE = {'null': True, 'blank': True}
# Create your models here.
class Blog(models.Model):
    """
    Модель блога
    """

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Содержание')
    image = models.ImageField(upload_to='products/', verbose_name='Превью')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    is_published = models.BooleanField(default=True, verbose_name='Статус публикации')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

    def add_view(self):
        self.views_count += 1
        self.save()