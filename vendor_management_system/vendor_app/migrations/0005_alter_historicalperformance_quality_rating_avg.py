# Generated by Django 4.2.7 on 2023-11-21 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0004_historicalperformance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalperformance',
            name='quality_rating_avg',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
