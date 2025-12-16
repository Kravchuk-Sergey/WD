from django.shortcuts import render
from django.shortcuts import render
from .models import Category

def index(request):
    categories = Category.objects.all()
    return render(request, 'shop/index.html', {'categories': categories})