# Generated by Django 4.2.9 on 2024-01-07 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TourManager', '0011_alter_buyercompany_short_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operation',
            old_name='follow_staf',
            new_name='follow_staff',
        ),
        migrations.RenameField(
            model_name='operation',
            old_name='selling_staf',
            new_name='selling_staff',
        ),
    ]
