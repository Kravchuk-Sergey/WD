from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CategoryForm, ProductForm
from .models import Category, Product
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

def index(request):
    categories = Category.objects.all()
    return render(request, 'shop/categories.html', {'categories': categories})

def category_list(request):
    categories = Category.objects.all()
    paginator = Paginator(categories, 10)  # 10 на сторінку
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop/categories.html', {'categories': page_obj, 'page_obj': page_obj})

def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop/products.html', {'products': page_obj, 'page_obj': page_obj})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    return render(request, 'shop/create_category.html', {'form': form})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    return render(request, 'shop/create_product.html', {'form': form})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'shop/category_detail.html', {'category': category})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})

def update_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'shop/update_category.html', {'form': form})

def update_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/update_product.html', {'form': form})

def delete_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        category.delete()
        return redirect('categories')
    return render(request, 'shop/delete_category.html', {'category': category})

def delete_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    return render(request, 'shop/delete_product.html', {'product': product})