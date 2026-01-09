from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')       # Показуємо назву та дату створення
    list_display_links = ('title',)             # Клік по назві відкриває запис на редагування
    list_filter = ('created_at',)               # Фільтр за датою створення
    search_fields = ('title',)                  # Пошук за назвою категорії
    # НЕ ставимо list_editable — бо редагувати created_at неможливо,
    # а title вже є посиланням (list_display_links)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'product_qty', 'category', 'created_at')
    list_display_links = ('title',)             # Клік по назві товару відкриває запис
    list_editable = ('price', 'product_qty')    # ТІЛЬКИ ці поля можна редагувати прямо в списку
    list_filter = ('category', 'created_at')    # Фільтри за категорією та датою
    search_fields = ('title',)                  # Пошук за назвою товару