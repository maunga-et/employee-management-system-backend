# Generated by Django 5.0.7 on 2024-07-20 15:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0002_leaverequest_date_created_leaverequest_date_updated_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='reviewed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='status',
            field=models.CharField(blank=True, choices=[('APPROVED', 'APPROVED'), ('DENIED', 'DENIED'), ('PENDING', 'PENDING')], default='PENDING', max_length=255, null=True),
        ),
    ]
