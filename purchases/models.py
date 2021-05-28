from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField
from django.utils import timezone
from django.urls import reverse

import uuid
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from products.models import Product
from webshop import settings


class Shipping(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = EmailField()

    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)
    home_address = models.CharField(max_length=50)
    name = models.CharField(max_length=30)


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    card_number = models.CharField(max_length=20)
    card_expiry_date = models.DateField()
    card_security_number = models.CharField(max_length=5)
    card_owner_name = models.CharField(max_length=30)


class Purchase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    # Displayed for both purchase sides

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    purchase_date = models.DateTimeField(default=timezone.now)

    amount = models.IntegerField(default=1, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=False)

    def get_absolute_url(self):
        return reverse("purchase-details", kwargs={"uuid": self.pk})

    def get_full_price(self):
        return self.amount * self.product.price


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    addition_date = models.DateTimeField(default=timezone.now)

    amount = models.IntegerField(default=1, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=False)
    
    def get_absolute_url(self):
        return reverse("cart", kwargs={"uuid": self.pk})

    def get_full_price(self):
        return self.amount * self.product.price

    
