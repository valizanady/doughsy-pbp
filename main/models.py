import uuid
from django.db import models

class Product(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]

    CATEGORY_CHOICES = [
        ('Donut', 'Donut'),
        ('Cheesecake', 'Cheesecake'),
        ('Cookies', 'Cookies'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Donut') 
    price = models.IntegerField()
    description = models.TextField()
    topping = models.CharField(max_length=50, default='', blank=True)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES, default='M')
    availability = models.BooleanField(default=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.item_name
