# Generated by Django 4.2.9 on 2024-01-07 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TourManager', '0006_operationitem_activity_cost_operationitem_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='city',
        ),
    ]
