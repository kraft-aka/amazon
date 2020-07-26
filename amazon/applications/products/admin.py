from django.contrib import admin

from .models import Product, ProductItem, ProductItemImage


class ImageInline(admin.TabularInline):
    model = ProductItemImage
    extra = 0


class ProductItemInline(admin.TabularInline):
    model = ProductItem
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductItemInline]


class ProductItemAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductItem, ProductItemAdmin)
