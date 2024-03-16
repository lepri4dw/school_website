from django.db import models

class Teacher(models.Model):
    CATEGORY = (
        ('Учитель', 'Учитель'),
        ('Администрация', 'Администрация'),
        ('Директор', 'Директор')
    )
    name = models.CharField(max_length=100, verbose_name='Введите ФИО')
    category = models.CharField(max_length=100, choices=CATEGORY, verbose_name='Выберите категорию')
    profession = models.CharField(max_length=100, verbose_name='Введите полное название должности')
    photo = models.ImageField(blank=True, upload_to='teachers/', verbose_name='Фото')

    def __str__(self):
        return self.name