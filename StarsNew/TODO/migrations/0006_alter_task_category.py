# Generated by Django 4.1 on 2024-08-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0005_rename_do_date_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('Fun', 'Tech'), ('Business', 'Work'), ('Personal', 'Teaching')], default='pending', max_length=20),
        ),
    ]
