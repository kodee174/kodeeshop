from django.db import models
from app.cores.date import get_today_datetime


class DiscountType(models.TextChoices):
    Percent = 'Percent'
    Price = 'Price'
    Free_ship = 'Free ship'


class DiscountManager(models.Manager):
    pass


class Discount(models.Model):
    class Meta:
        db_table = 'discount'
        default_related_name = 'discount'

    code = models.CharField(max_length=150, null=False, blank=False)
    type = models.CharField(
        max_length=9,
        choices=DiscountType.choices,
        default=DiscountType.Percent
    )
    rate = models.FloatField(max_length=11, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    apply_date = models.DateTimeField(null=False, blank=False)
    expiry_date = models.DateTimeField(default=None)
    create_at = models.DateTimeField(default=get_today_datetime(), null=True, blank=True)
    update_at = models.DateTimeField(default=None, null=True, blank=True)
    objects = DiscountManager()
