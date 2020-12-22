from django.db import models

from app.cores.date import get_today_datetime
from app.models.product import Product


class ProductVariantName(models.TextChoices):
    Color = 'Color'
    Size = 'Size'
    Material = 'Material'

class ProductVariantManager(models.Manager):
    pass


class ProductVariant(models.Model):
    class Meta:
        db_table = 'product_variant'
        default_related_name = 'product_variant'

    name = models.CharField(
        max_length=250,
        choices=ProductVariantName.choices
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    create_at = models.DateTimeField(default=get_today_datetime(), null=True, blank=True)
    update_at = models.DateTimeField(default=None, null=True, blank=True)
    objects = ProductVariantManager()
