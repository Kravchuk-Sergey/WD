from django import forms
from .models import Category, Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва категорії',
            }),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'product_qty', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва товару'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ціна товару'}),
            'product_qty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Кількість товару'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }