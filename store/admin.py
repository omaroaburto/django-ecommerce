from django.contrib import admin
from .models import Product, Variation

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('pro_name','pro_price','pro_stock','category','modified_date','is_available')
    prepopulated_fields = {'pro_slug':('pro_name',)}

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','variation_category','variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product','variation_category','variation_value', 'is_active')
# Register your models here.
admin.site.register(Product, ProductoAdmin)
admin.site.register(Variation, VariationAdmin)