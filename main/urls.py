from django.urls import path
from .views import *

urlpatterns = [
    path('',main_page,name='index_url'),
    path('category/',category,name='category_url'),
    path('product/<slug:slug>',product,name='product_url'),
    path('products/',products_all,name='products_url'),
    path('registration/',register_page,name='register_url')
]