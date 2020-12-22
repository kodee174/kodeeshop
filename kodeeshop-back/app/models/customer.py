from django.db import models
from django.db.models import Q

from app.models.customer_shipment import CustomerShipment
from app.cores.date import get_today_datetime


class CustomerGender(models.TextChoices):
    Male = 'Male'
    Female = 'Female'


class CustomerManager(models.Manager):

    def get_customer_by_email_or_phone(self, email, phone):
        if email:
            return self.get_queryset().filter(Q(email=email) | Q(phone=phone)).values().first()
        return self.get_queryset().filter(phone=phone).values().first()

    def get_customer_by_id(self, id):
        return self.get_queryset().filter(id=id).values().first()

    def create_customer(self, data):
        return self.create(**data)

    def update_customer_by_id(self, data, id):
        return self.get_queryset().filter(id=id).update(**data, update_at=get_today_datetime())

    def delete_customer_by_id(self, id):
        customer = self.get_queryset().get(id=id)
        customer.customer_shipment.delete()
        customer.delete()
        return customer


class Customer(models.Model):
    class Meta:
        db_table = 'customer'
        default_related_name = 'customer'

    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=250, unique=True, null=True, blank=True)
    password = models.CharField(max_length=250, null=False, blank=False)
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=12, unique=True, null=False, blank=False)
    gender = models.CharField(
        max_length=6,
        choices=CustomerGender.choices,
        default=CustomerGender.Female
    )
    customer_shipment = models.ForeignKey(
        CustomerShipment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    create_at = models.DateTimeField(default=get_today_datetime(), null=True, blank=True)
    update_at = models.DateTimeField(default=None, null=True, blank=True)
    objects = CustomerManager()
