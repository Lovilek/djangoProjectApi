# Generated by Django 4.2.5 on 2023-09-26 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0002_alter_lesson_time_alter_viewinghistory_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='viewinghistory',
            name='time',
            field=models.IntegerField(),
        ),
    ]
