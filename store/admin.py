from django.contrib import admin
from .models import Product

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('pro_name','pro_price','pro_stock','category','modified_date','is_available')
    prepopulated_fields = {'pro_slug':('pro_name',)}

# Register your models here.
admin.site.register(Product, ProductoAdmin)