from django.db import models
from app.models.order import Order
from app.models.order_product import OrderProduct


class OrderOrderProductManager(models.Manager):
    pass


class OrderOrderProduct(models.Model):
    class Meta:
        db_table = 'order_order_product'
        default_related_name = 'order_order_product'
        
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    order_product = models.ForeignKey(
        OrderProduct,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    objects = OrderOrderProductManager()
