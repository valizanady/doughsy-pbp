from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()


    def __str__(self):
        return self.name

class Donut(models.Model):
    flavor = models.CharField(max_length=50)  
    size = models.CharField(max_length=10)    
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.flavor} ({self.size})"
