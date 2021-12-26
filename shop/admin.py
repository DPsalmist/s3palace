from django.contrib import admin

# Register your models here.
from .models import Category, Shoes, Suits, Sub_Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Sub_Category)
class Sub_CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'sizes', 'category', 'brands', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'category', 'brands', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'category', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Suits)
class SuitsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'sizes', 'category', 'brands', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'category', 'brands', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

# @admin.register(Review)
# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'product', 'created', 'active')
#     list_filter = ('active', 'created', 'updated')
#     search_fields = ('name', 'email', 'body')