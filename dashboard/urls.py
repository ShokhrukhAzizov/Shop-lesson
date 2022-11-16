from django.urls import path
from .views import *

urlpatterns = [
    path('', dashborad_view, name='dashboard_url'),
    path('categories/', categories_view, name='categories_url'),
    path('category/update/', category_update, name='category_update_url'),
    path('category/delete/',category_delete, name='category_delete_url'),
    path('products/view',product_page,name='products_page_url'),
    path('product/delete/',product_delete,name='products_delete_url')
]