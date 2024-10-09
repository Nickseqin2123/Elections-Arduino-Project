# Generated by Django 5.1.1 on 2024-10-09 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_electionmodel_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choicemodel',
            name='election',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='main.electionmodel', verbose_name='Голосования'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='main.choicemodel', verbose_name='Выборы ответов'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='election',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='main.electionmodel', verbose_name='Голосования'),
        ),
    ]
