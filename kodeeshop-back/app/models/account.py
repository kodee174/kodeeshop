from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from app.cores.date import get_today_datetime


class AccountManager(UserManager):
    pass


class Account(AbstractUser):
    class Meta:
        db_table = 'account'
        default_related_name = 'account'

    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    password = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(max_length=250, unique=True, null=False, blank=False)
    create_at = models.DateTimeField(default=get_today_datetime(), null=True, blank=True)
    update_at = models.DateTimeField(default=None, null=True, blank=True)
    objects = AccountManager()
