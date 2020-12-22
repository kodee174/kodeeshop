from django.db import models
from app.models.customer import Customer
from app.models.order_product import OrderProduct
from app.models.order_shipment import OrderShipment
from app.cores.date import get_today_datetime


class OrderShipmentStatus(models.TextChoices):
    Not_Ship = 'Not ship'
    Shipping = 'Shipping'
    Shipped = 'Shipped'


class OrderPaymentStatus(models.TextChoices):
    Not_Pay = 'Not pay'
    Paying = 'Paying'
    Paid = 'Paid'


class OrderManager(models.Manager):
    pass


class Order(models.Model):
    class Meta:
        db_table = 'order'
        default_related_name = 'order'

    shipment_status = models.CharField(
        max_length=8,
        choices=OrderShipmentStatus.choices,
        default=OrderShipmentStatus.Not_Ship
    )
    payment_status = models.CharField(
        max_length=7,
        choices=OrderPaymentStatus.choices,
        default=OrderPaymentStatus.Not_Pay
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    order_product = models.ManyToManyField(
        OrderProduct,
        through='OrderOrderProduct',

    ),
    order_shipment = models.ForeignKey(
        OrderShipment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    create_at = models.DateTimeField(default=get_today_datetime(), null=True, blank=True)
    update_at = models.DateTimeField(default=None, null=True, blank=True)
    objects = OrderManager()
