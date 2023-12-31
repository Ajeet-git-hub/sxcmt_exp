# Generated by Django 4.2.3 on 2023-07-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='name',
        ),
        migrations.AddField(
            model_name='book',
            name='book_author',
            field=models.CharField(default='one', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_code',
            field=models.CharField(default='pro', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_publisher',
            field=models.CharField(default='pub', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_title',
            field=models.CharField(default='he', max_length=100),
            preserve_default=False,
        ),
    ]
