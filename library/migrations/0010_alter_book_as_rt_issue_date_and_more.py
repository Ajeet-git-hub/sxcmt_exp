# Generated by Django 4.2.3 on 2023-07-31 21:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_book_as_rt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_as_rt',
            name='issue_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='book_as_rt',
            name='recovery_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 15, 21, 11, 12, 149006, tzinfo=datetime.timezone.utc)),
        ),
    ]