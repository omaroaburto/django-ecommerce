from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import Category
# Create your views here.
def store(request, cat_slug=None):
    categories = None
    products= None

    if cat_slug!=None:
        categories = get_object_or_404(Category, cat_slug=cat_slug)
        products = Product.objects.filter(category=categories, is_available= True)
        product_count = products.count()
    else:
        products =  Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count
    }

    return render(request, 'store/store.html', context)
