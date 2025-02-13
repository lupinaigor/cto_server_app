from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category': self.category,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
