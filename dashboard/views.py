from django.shortcuts import render, redirect
from main.models import*
from django.contrib.auth.decorators import login_required


@login_required(login_url='register_url')
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

@login_required(login_url='register_url')
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

@login_required
def category_update(request):
    name = request.POST['name']
    id = request.POST['id']
    category = Category.objects.get(id=id)
    category.title=name
    category.save()
    return redirect('categories_url')

@login_required
def category_delete(request):
    id = request.POST['id']
    category = Category.objects.get(id=id)
    category.delete()    
    return redirect('categories_url')

@login_required
def product_page(request):
    categorys = Category.objects.all()
    products = Product.objects.all()[:5]
    
    if request.method == 'POST':
        
        company = request.POST['company']
        name = request.POST['name']
        descritpion = request.POST['description']
        file = request.POST['file']
        price = request.POST['price']
        category = request.POST['category']
        category = Category.objects.get(id=category)
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
            'categorys':categorys,
            'products':products
            
        }
        
    return render(request, 'dashboard/products.html',context)


@login_required
def product_delete(request):
    id = request.POST['id']
    products = Product.objects.get(id=id)
    products.delete()
    return redirect('products_page_url')
   

def query(request):
    q = request.GET.get('q')
    products = Product.objects.filter(name__icontains =q)
    categorys = Category.objects.filter(title__icontains=q)
    comment = Comment.objects.filter(comment__icontains=q)

    context = {
        'products':products,
        'categorys':categorys,
        'comment':comment
    }

    return render(request, 'dashboard/search.html', context)

