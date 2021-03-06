
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.urls import reverse
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

    def get_url(self):
        return reverse('product_detail',args=[self.category.cat_slug, self.pro_slug])

    def __str__(self):
        return self.pro_name

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def tallas(self):
        return super(VariationManager, self).filter(variation_category='talla', is_active=True)      

variation_category_choice = (
    ('color','color'),
    ('talla','talla'),
)

class Variation(models.Model):
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_category+':'+self.variation_value