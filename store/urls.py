from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('<slug:cat_slug>', views.store, name='products_by_category'),
]