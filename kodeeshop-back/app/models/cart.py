from django.db import models
from app.cores.date import get_today_datetime
from app.models.customer import Customer
from app.models.product import Product


class CartManager(models.Manager):
    pass


class Cart(models.Model):
    class Meta:
        db_table = 'cart'
        default_related_name = 'cart'

    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    quantity = models.IntegerField(null=False, blank=False)
    create_at = models.DateTimeField(default=get_today_datetime(), null=True, blank=True)
    update_at = models.DateTimeField(default=None, null=True, blank=True)
    objects = CartManager()
