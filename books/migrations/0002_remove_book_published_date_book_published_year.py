# Generated by Django 5.1.1 on 2024-10-16 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='published_date',
        ),
        migrations.AddField(
            model_name='book',
            name='published_year',
            field=models.PositiveIntegerField(default=2000),
            preserve_default=False,
        ),
    ]
