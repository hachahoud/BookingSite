# Generated by Django 3.1.1 on 2020-09-21 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_auto_20200921_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingtime',
            name='start_time',
            field=models.PositiveSmallIntegerField(choices=[('08', '08')], default='08'),
        ),
    ]