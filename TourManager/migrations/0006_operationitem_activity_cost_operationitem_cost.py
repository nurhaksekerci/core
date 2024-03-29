# Generated by Django 4.2.9 on 2024-01-07 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TourManager', '0005_activitysupplier_activitycost'),
    ]

    operations = [
        migrations.AddField(
            model_name='operationitem',
            name='activity_cost',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TourManager.activitycost', verbose_name='Aktivite Tedarikçi'),
        ),
        migrations.AddField(
            model_name='operationitem',
            name='cost',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TourManager.cost', verbose_name='Araç Tedarikci'),
        ),
    ]
