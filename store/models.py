from audioop import reverse
from django.db import models
from category.models import Category

# Create your models here.
class Product(models.Model):
    pro_name = models.CharField(max_length=200, unique=True)
    pro_slug = models.CharField(max_length=200, unique=True)
    pro_description = models.TextField(max_length=500, blank=True)
    pro_price = models.IntegerField()
    pro_images = models.ImageField(upload_to='photos/products')
    pro_stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pro_name

