from django.shortcuts import redirect, render
from .models import *
from django.db.models import Q
# from django.contrib.auth.models import User
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def main_page(request):
    return render(request,'main/index.html')

def category(request):
    categorys = Category.objects.all()
    
   
    context = {
        'categorys':categorys,
       
    }
    return render(request,'main/category.html',context)

def product(request,slug):
    categorys = Category.objects.all()
    products = Product.objects.all()
    category = Category.objects.get(slug=slug)
    product = Product.objects.filter(category=category)
    
    
    context = {
        'categorys':categorys,
        'products':products,
        'category':category,
        'product':product
    }
    return render(request,'main/product.html',context)
    

def register_page(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password'] 
        if User.objects.filter(username=username).count() == 0:
            User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            usr = authenticate(username=username,password=password)
            login(request,usr)
            return redirect('index_url')
        else:
            messages.error(request,'Username already registred')
            return redirect('register_url')

    return render(request,'main/register-page.html')

