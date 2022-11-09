from django.urls import path
from .views import *

urlpatterns = [
    path('',main_page,name='index_url'),
    path('categorys/', categorys, name='category_url'),
    path('category/detail/<int:pk>/', category_detail, name='category_detail_url'),
    path('products/',products, name='products_url'),
    path('product/detail/<int:pk>/', product_detail, name='product_detail_url'),
    path('registration/',register_page,name='register_url')
]