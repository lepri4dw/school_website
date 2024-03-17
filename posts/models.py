from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    image = models.ImageField(upload_to='posts/', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

