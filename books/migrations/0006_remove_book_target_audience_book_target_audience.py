# Generated by Django 5.1.1 on 2024-10-23 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_targetaudience_alter_book_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='target_audience',
        ),
        migrations.AddField(
            model_name='book',
            name='target_audience',
            field=models.ManyToManyField(blank=True, to='books.targetaudience'),
        ),
    ]
