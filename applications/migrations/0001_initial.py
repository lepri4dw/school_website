# Generated by Django 4.2.11 on 2024-03-17 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_name', models.CharField(max_length=100, verbose_name='Имя родителя')),
                ('phone_number', models.CharField(max_length=13, verbose_name='Телефон для связи (0555555555 или +996555555555)')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО ребенка')),
                ('birth_date', models.DateField(verbose_name='Дата рождения ребенка')),
                ('class_number', models.PositiveIntegerField(verbose_name='Класс для поступления')),
                ('previous_school', models.CharField(blank=True, max_length=255, verbose_name='Предыдущая школа')),
            ],
        ),
    ]