# Generated by Django 4.2.11 on 2024-03-17 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='phone_number',
            field=models.CharField(max_length=13, verbose_name='Телефон для связи (+996555555555)'),
        ),
    ]
