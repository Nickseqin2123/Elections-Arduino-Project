# Generated by Django 5.1.1 on 2025-01-16 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElectionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True, verbose_name='Имя')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания')),
            ],
        ),
    ]
