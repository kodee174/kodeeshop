from django.db import models

from app.cores.date import get_today_datetime


class CustomerCountry(models.TextChoices):
    Viet_Nam = 'Viet Nam'


class CustomerCity(models.TextChoices):
    Ha_Noi = 'Ha Noi'
    Ho_Chi_Minh = 'Ho Chi Minh'
    Phu_Tho = 'Phu Tho'


class CustomerDistrict(models.TextChoices):
    Cau_Giay = 'Cau Giay'
    Nam_Tu_Liem = 'Nam Tu Liem'
    Bac_Tu_Liem = 'Bac Tu Liem'


class CustomerShipmentManager(models.Manager):

    def create_customer_shipment(self, data):
        return self.create(**data)

    def get_customer_shipment_by_id(self, id):
        return self.get_queryset().filter(id=id).values().first()

    def update_customer_shipment_by_id(self, data, id):
        return self.get_queryset().filter(id=id).update(**data, update_at=get_today_datetime())

class CustomerShipment(models.Model):
    class Meta:
        db_table = 'customer_shipment'
        default_related_name = 'customer_shipment'

    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    country = models.CharField(
        max_length=30,
        choices=CustomerCountry.choices,
        null=True,
        blank=True
    )
    city = models.CharField(
        max_length=30,
        choices=CustomerCity.choices,
        null=True,
        blank=True
    )
    district = models.CharField(
        max_length=30,
        choices=CustomerDistrict.choices,
        null=True,
        blank=True
    )
    create_at = models.DateTimeField(default=get_today_datetime(), null=True, blank=True)
    update_at = models.DateTimeField(default=None, null=True, blank=True)
    objects = CustomerShipmentManager()
