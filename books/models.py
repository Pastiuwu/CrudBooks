from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year = models.PositiveIntegerField()

    
    in_stock = models.BooleanField(default=True)
    
# (select)    
    CATEGORIES_CHOICES = [
        ('Novela', 'Novela'),
        ('Ciencia Ficción', 'Ciencia Ficción'),
        ('Política', 'Política'),
        ('Historia', 'Historia'),
        ('Comic', 'Comic'),
    ]
    categories = models.CharField(max_length=50, choices=CATEGORIES_CHOICES, blank=True)
    
 # (check group)   
    TARGET_AUDIENCE_CHOICES = [
        ('Adulto', 'Adulto'),
        ('Joven', 'Joven'),
        ('Niño', 'Niño'),
        ('Universitario', 'Universitario'),
    ]
    target_audience = models.CharField(max_length=50, choices=TARGET_AUDIENCE_CHOICES, blank=True)
    
    def __str__(self):
        return self.title
