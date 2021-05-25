from abc import abstractclassmethod
from functools import total_ordering
from django.db import models
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from .managers import UserManager
from products.models import Product
from purchases.models import Purchase


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(_('email address'), unique=True, null=True, blank=False)
    username = models.CharField(_('username'), max_length=40, unique=True, null=True, blank=False)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    money_spent = models.DecimalField(decimal_places=2, max_digits=9, default = 0.00)
    bought_products = models.ManyToManyField(Product, through=Purchase)

    def __str__(self):
        return str(self.username)
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
