# Generated by Django 3.1.1 on 2020-09-18 23:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='full',
        ),
        migrations.AlterField(
            model_name='bookingdate',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 19, 0, 33, 14, 530716)),
        ),
    ]
