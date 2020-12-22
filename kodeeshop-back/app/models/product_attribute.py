from django.db import models
from app.cores.date import get_today_datetime
from app.models.product import Product


class ProductAttributeManager(models.Manager):
    pass


class ProductAttribute(models.Model):
    class Meta:
        db_table = 'product_attribute'
        default_related_name = 'product_attribute'

    name = models.CharField(max_length=250, null=False, blank=False)
    primary_price = models.FloatField(max_length=11, null=True, blank=True)
    sale_price = models.FloatField(max_length=11, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False)
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    create_at = models.DateTimeField(default=get_today_datetime(), null=True, blank=True)
    update_at = models.DateTimeField(default=None, null=True, blank=True)
    objects = ProductAttributeManager()
