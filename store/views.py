from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.db.models import Q
from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id


# Create your views here.
def store(request, cat_slug=None):
    categories = None
    products= None

    if cat_slug!=None:
        categories = get_object_or_404(Category, cat_slug=cat_slug)
        products = Product.objects.filter(category=categories, is_available= True).order_by("-id")
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products =  Product.objects.all().filter(is_available=True).order_by("-id")
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count
    }

    return render(request, 'store/store.html', context)

def product_detail(request, cat_slug, pro_slug):
    try:
        single_product = Product.objects.get(category__cat_slug=cat_slug, pro_slug=pro_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as E:
        raise E
    
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request,'store/product_detail.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by("-created_date").filter(Q(pro_description__icontains=keyword) | Q(pro_name__icontains=keyword))
            product_count= products.count()
        else:
            products = None
            product_count = 0
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request,'store/store.html', context)