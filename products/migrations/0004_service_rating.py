# Generated by Django 3.1.3 on 2020-12-06 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201206_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]