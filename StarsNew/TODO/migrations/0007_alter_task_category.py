# Generated by Django 4.1 on 2024-08-28 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0006_alter_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('fun', 'Fun'), ('business', 'Business'), ('personal', 'Personal'), ('tech', 'Technology')], default='Teaching', max_length=20),
        ),
    ]
