# Generated by Django 3.1.3 on 2021-01-14 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='likes',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='views',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True),
        ),
    ]
