# Generated by Django 5.1.1 on 2024-10-11 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electionmodel',
            name='name',
            field=models.CharField(max_length=254, unique=True, verbose_name='Имя'),
        ),
    ]
