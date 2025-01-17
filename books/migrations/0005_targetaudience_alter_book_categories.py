# Generated by Django 5.1.1 on 2024-10-23 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_remove_book_attribute_remove_book_genre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TargetAudience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Adulto', 'Adulto'), ('Joven', 'Joven'), ('Niño', 'Niño'), ('Universitario', 'Universitario')], max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='categories',
            field=models.CharField(blank=True, choices=[('Novela', 'Novela'), ('Ciencia Ficción', 'Ciencia Ficción'), ('Política', 'Política'), ('Historia', 'Historia'), ('Comic', 'Comic')], max_length=50),
        ),
    ]
