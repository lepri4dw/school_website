from django.db import models

class Application(models.Model):
    parent_name = models.CharField(max_length=100, verbose_name='Имя родителя')
    phone_number = models.CharField(max_length=13, verbose_name='Телефон для связи (+996555555555)')
    full_name = models.CharField(max_length=100, verbose_name='ФИО ребенка')
    birth_date = models.DateField(verbose_name='Дата рождения ребенка')
    class_number = models.PositiveIntegerField(verbose_name='Класс для поступления')
    previous_school = models.CharField(max_length=255, verbose_name='Предыдущая школа', blank=True)

    def __str__(self):
        return self.full_name
