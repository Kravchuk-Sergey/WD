from django.db import models
from django.utils.text import slugify   # Додай цей імпорт наверху файлу


class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:  # Якщо slug порожній — генеруємо з title
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['title']
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    price = models.FloatField()
    product_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    image_name = models.CharField(max_length=255, blank=True, null=True, help_text="Назва товару")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['title']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'