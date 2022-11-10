from django.shortcuts import render
from main.models import*
from django.contrib.auth import logout


def dashborad_view(request):
    user_quantity = User.objects.all().count()
    product_available_quantity = Product.objects.filter(available=True).count()
    product_not_ava_quantity = Product.objects.filter(available=False).count()
    products = Product.objects.all()[:5]
    category_quantity = Category.objects.all().count()
    context = {
        'user_quantity':user_quantity,
        'product_available_quantity':product_available_quantity,
        'product_not_ava_quantity':product_not_ava_quantity,
        'category_quantity':category_quantity,
        'products':products
    }
    return render(request, 'dashboard/index.html', context)

def logout(request):
    return render(request,logout)