from django.db import models
from django.urls import reverse

from .managers import *
from .choices import *

from applications.categories.models import Category

from applications.authors.models import Profile


class Product(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name='products')
    image = models.ImageField(upload_to='products_images', default='product.jpg')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ('-id',)


class ProductItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    color = models.CharField(choices=PRODUCT_COLORS, max_length=15)
    size = models.CharField(choices=PRODUCT_SIZES, max_length=4)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    objects = ProductItemManager()
    instock = InStockManager()

    def __str__(self):
        return f'SIZE: {self.size}. COLOR: {self.color}. PRICE: {self.price} USD'

    def get_absolute_url(self):
        return reverse('item-list', kwargs={'pk': self.pk})
    

class ProductItemImage(models.Model):
    image = models.ImageField(upload_to='productItemImages')
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='images')
