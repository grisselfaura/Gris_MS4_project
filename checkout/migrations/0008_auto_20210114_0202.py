# Generated by Django 3.1.3 on 2021-01-14 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20210105_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='select_date',
            field=models.DateTimeField(blank=True, verbose_name='Selected Date (mm/dd/yyyy)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
