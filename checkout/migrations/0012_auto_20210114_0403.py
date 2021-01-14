# Generated by Django 3.1.3 on 2021-01-14 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0011_remove_order_select_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='select_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Selected Date (mm/dd/yyyy)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]