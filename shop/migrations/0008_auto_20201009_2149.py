# Generated by Django 3.1 on 2020-10-09 16:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20201009_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_place',
            name='delivery_user',
            field=models.CharField(default='Will be Updated Soon', max_length=100),
        ),
        migrations.AlterField(
            model_name='order_place',
            name='order_place_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 9, 16, 19, 13, 510411, tzinfo=utc)),
        ),
    ]
