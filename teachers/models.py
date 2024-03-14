from django.db import models

class Teacher(models.Model):
    CATEGORY = (
        ('Учитель', 'Учитель'),
        ('Администрация', 'Администрация'),
        ('Директор', 'Директор')
    )
    name = models.CharField(max_length=100, verbose_name='Введите ФИО')
    profession = models.CharField(max_length=100, verbose_name='Введите полное название должности')
    photo = models.ImageField(upload_to='teachers/')

    def __str__(self):
        return self.name