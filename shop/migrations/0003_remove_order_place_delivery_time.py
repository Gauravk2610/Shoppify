# Generated by Django 3.1 on 2020-10-09 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20201008_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_place',
            name='delivery_time',
        ),
    ]
