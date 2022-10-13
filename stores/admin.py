from django.contrib import admin

# Register your models here.
from .models import Category, Tag, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'date_created', 'date_updated', 'owner')
    list_filter = ('category', 'tags')
    search_fields = ('name', 'description')
    list_per_page = 20
    

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product, ProductAdmin)


