from django.db import models
from app.cores.date import get_today_datetime
from app.models.product import Product

class ProductImageManager(models.Manager):
    pass


class ProductImage(models.Model):
    class Meta:
        db_table = 'product_image'
        default_related_name = 'product_image'

    slug = models.CharField(max_length=250, null=False, blank=False)
    default = models.BooleanField(default=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    create_at = models.DateTimeField(default=get_today_datetime(), null=True, blank=True)
    update_at = models.DateTimeField(default=None, null=True, blank=True)
