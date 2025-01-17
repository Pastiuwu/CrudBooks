# Generated by Django 5.1.1 on 2024-10-23 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_attribute_book_categories_book_in_stock_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='attribute',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AlterField(
            model_name='book',
            name='target_audience',
            field=models.CharField(blank=True, choices=[('Adulto', 'Adulto'), ('Joven', 'Joven'), ('Niño', 'Niño'), ('Universitario', 'Universitario')], max_length=50),
        ),
    ]
