import uuid
from decimal import Decimal

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from products.models import Product
from purchases.models import Purchase, Cart
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    date_joined = models.DateTimeField(default=timezone.now)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    certified = models.BooleanField(default=False)

    # Publicly available data

    email = models.EmailField(unique=True, null=True, blank=False)
    username = models.CharField(max_length=40, unique=True, null=True, blank=False)

    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    # Dashboard data

    money_spent = models.DecimalField(decimal_places=2, max_digits=9, default=0.00)
    bought_products = models.ManyToManyField(Product, through=Purchase, related_name='bought_user')
    cart_products = models.ManyToManyField(Product, through=Cart, related_name='cart_user')

    def __str__(self):
        return str(self.username)

    @property
    def rating(self):
        try:
            rating = 0
            iteration = 0
            for product in Product.objects.all().filter(seller=self):
                rating += product.rating
                iteration += 1
            rating = Decimal(rating / iteration)
            return round(rating, 1)
        except:
            return round(Decimal(0 / 1), 1)

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_certified(self):
        return self.certified

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return f'{self.first_name}'
