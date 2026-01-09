from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.category_list, name='categories'),
    path('products/', views.product_list, name='products'),
    path('categories/create/', views.create_category, name='category-create'),
    path('products/create/', views.create_product, name='product-create'),
    path('categories/<slug:slug>/', views.category_detail, name='category-detail'),
    path('products/<slug:slug>/', views.product_detail, name='product-detail'),
    path('categories/<slug:slug>/update/', views.update_category, name='category-update'),
    path('products/<slug:slug>/update/', views.update_product, name='product-update'),
    path('categories/<slug:slug>/delete/', views.delete_category, name='category-delete'),
    path('products/<slug:slug>/delete/', views.delete_product, name='product-delete'),
]