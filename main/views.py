from django.shortcuts import redirect, render
from .models import *
from django.db.models import Q
# from django.contrib.auth.models import User
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def main_page(request):
    return render(request,'main/index.html')


def categorys(request):
    categorys = Category.objects.all()
    context = {
        'categorys':categorys
    }
    return render(request, 'main/category.html', context)


def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    products = Product.objects.filter(category=category)
    context = {
        'category':category,
        'products':products
    }
    return render(request, 'main/category-detail.html', context)


def products(request):
    products = Product.objects.all()
    q = request.GET.get('name')
    if q is not None and q!= '':
        products = Product.objects.filter(Q(name__icontains=q))

    context = {
        'products':products
    }
    return render(request, 'main/products.html', context)


def product_detail(request, pk):
    
    product = Product.objects.get(pk=pk)
    comment = Comment.objects.filter(product=product)
    
    
    context = {
        'product':product,
        'comment':comment,
        
    }
    
    if request.method == 'POST':
        a = request.POST['comment']
        Comment.objects.create(
            comment=a,
            product=product
        )
    
    return render(request, 'main/product-detail.html', context)


def register_page(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password'] 
        phone = request.POST['phone'] 
        try:
            User.objects.create_user(
                username=username,
                email=email,
                password=password,
                phone=phone
            )
            usr = authenticate(username=username,password=password)
            login(request,usr)
            return redirect('index_url')
        except:
            messages.error(request,'Username already registred')
            return redirect('register_url')

    return render(request,'main/register-page.html')

