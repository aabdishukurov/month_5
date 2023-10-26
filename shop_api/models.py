from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.CharField(max_length=225)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews'),

    def __str__(self):
        return self.text
