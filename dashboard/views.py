from django.shortcuts import render, redirect
from main.models import*


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


def categories_view(request):
    categorys = Category.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        Category.objects.create(
            title=name,
            slug=name
        )
    context = {
        'categorys':categorys
    }
    return render(request, 'dashboard/categories.html', context)


def category_update(request):
    name = request.POST['name']
    id = request.POST['id']
    category = Category.objects.get(id=id)
    category.title=name
    category.save()
    return redirect('categories_url')


def category_delete(request):
    id = request.POST['id']
    category = Category.objects.get(id=id)
    category.delete()    
    return redirect('categories_url')


def product_page(request):
    products = Product.objects.all()
    category = Category.objects.filter(title=products)
    if request.method == 'POST':
        company = request.POST['company']
        name = request.POST['name']
        descritpion = request.POST['description']
        file = request.POST['file']
        price = request.POST['price']
        Product.objects.create(
            company=company,
            name=name,
            description=descritpion,
            image=file,
            price=price,
            slug=name,
            category=category
        )
    context = {
            'products':products,
            'category':category
        }
        
    return render(request, 'dashboard/products.html',context)