from django.db import models


class ProductItemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class InStockManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(quantity=0)