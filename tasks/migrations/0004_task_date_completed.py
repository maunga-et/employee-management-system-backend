# Generated by Django 5.0.7 on 2024-07-20 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
