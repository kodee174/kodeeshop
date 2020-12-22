from django.db import models

from app.cores.date import get_today_datetime
from app.models.product import Product
from app.models.product_attribute_value import ProductAttributeValue


class OrderProductManager(models.Manager):
    pass


class OrderProduct(models.Model):
    class Meta:
        db_table = 'order_product'
        default_related_name = 'order_product'

    title = models.CharField(max_length=250, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False)
    price = models.FloatField(max_length=11, null=False, blank=False)
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    product_attribute_value = models.ForeignKey(
        ProductAttributeValue,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    create_at = models.DateTimeField(default=get_today_datetime(), null=True, blank=True)
    update_at = models.DateTimeField(default=None, null=True, blank=True)
    objects = OrderProductManager()
