from django.db import models
from app.cores.date import get_today_datetime
from app.models.product import Product
from app.models.product_attribute import ProductAttribute
from app.models.product_variant import ProductVariant
from app.models.product_variant_value import ProductVariantValue


class ProductAttributeValueManager(models.Manager):
    pass


class ProductAttributeValue(models.Model):
    class Meta:
        db_table = 'product_attribute_value'
        default_related_name = 'product_attribute_value'

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    product_attribute = models.ForeignKey(
        ProductAttribute,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    product_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    product_variant_value = models.ForeignKey(
        ProductVariantValue,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    create_at = models.DateTimeField(default=get_today_datetime(), null=True, blank=True)
    update_at = models.DateTimeField(default=None, null=True, blank=True)
    objects = ProductAttributeValueManager()
