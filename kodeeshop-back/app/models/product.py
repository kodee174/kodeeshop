from django.db import models
from app.cores.date import get_today_datetime
from app.models.collection import Collection
from app.models.tag import Tag


class ProductManager(models.Manager):
    pass


class Product(models.Model):
    class Meta:
        db_table = 'product'
        default_related_name = 'product'

    title = models.CharField(max_length=250, null=False, blank=False)
    content = models.CharField(max_length=1000, null=False, blank=False)
    slug = models.CharField(max_length=250, unique=True, null=False, blank=False)
    tag = models.ManyToManyField(
        Tag,
        through='ProductTag'
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    create_at = models.DateTimeField(default=get_today_datetime(), null=True, blank=True)
    update_at = models.DateTimeField(default=None, null=True, blank=True)
    objects = ProductManager()
