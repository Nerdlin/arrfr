# Generated by Django 5.1.1 on 2024-11-04 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_telegramuser_age_telegramuser_benefits_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegramuser',
            name='total_requests',
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='used_functions',
            field=models.JSONField(default=list, verbose_name='Использованные функции'),
        ),
    ]