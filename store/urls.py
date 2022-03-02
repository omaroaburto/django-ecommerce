from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('category/<slug:cat_slug>/', views.store, name='products_by_category'),
    path('category/<slug:cat_slug>/<slug:pro_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name="search"),
]

