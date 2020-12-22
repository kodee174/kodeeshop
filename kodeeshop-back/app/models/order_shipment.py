from django.db import models

from app.cores.date import get_today_datetime


class OrderCountry(models.TextChoices):
    Viet_Nam = 'Viet Nam'

class OrderCity(models.TextChoices):
    Ha_Noi = 'Ha Noi'
    Ho_Chi_Minh = 'Ho Chi Minh'
    Phu_Tho = 'Phu Tho'

class OrderDistrict(models.TextChoices):
    Cau_Giay = 'Cau Giay'
    Nam_Tu_Liem = 'Nam Tu Liem'
    Bac_Tu_Liem = 'Bac Tu Liem'

class OrderShipmentManager(models.Manager):
    pass


class OrderShipment(models.Model):
    class Meta:
        db_table = 'order_shipment'
        default_related_name = 'order_shipment'

    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    country = models.CharField(
        max_length=30,
        choices=OrderCountry.choices,
        null=True,
        blank=True
        )
    city = models.CharField(
        max_length=30,
        choices=OrderCity.choices,
        null=True,
        blank=True
    )
    district = models.CharField(
        max_length=30,
        choices=OrderDistrict.choices,
        null=True,
        blank=True
    )
    create_at = models.DateTimeField(default=get_today_datetime(), null=True, blank=True)
    update_at = models.DateTimeField(default=None, null=True, blank=True)
    objects = OrderShipmentManager()
