from django.db import models
from app.models.product import Product
from app.models.tag import Tag


class ProductTagManager(models.Manager):
    pass


class ProductTag(models.Model):
    class Meta:
        db_table = 'product_tag'
        default_related_name = 'product_tag'

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    objects = ProductTagManager()
