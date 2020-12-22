from django.db import models

from app.cores.date import get_today_datetime
from app.models.product import Product
from app.models.product_image import ProductImage
from app.models.product_variant import ProductVariant


class ProductVariantValueManager(models.Manager):
    pass


class ProductVariantValue(models.Model):
    class Meta:
        db_table = 'product_variant_value'
        default_related_name = 'product_variant_value'

    name = models.CharField(max_length=250, null=False, blank=False)
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    product_image = models.ForeignKey(
        ProductImage,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    product_vartiant = models.ForeignKey(
        ProductVariant,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    create_at = models.DateTimeField(default=get_today_datetime(), null=True, blank=True)
    update_at = models.DateTimeField(default=None, null=True, blank=True)
    objects = ProductVariantValueManager()
