from django.db import models
from django.utils import timezone
import os, sys

from django.db.models.enums import Choices
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from products.models import Product
from webshop import settings


class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    amount = models.IntegerField(default=1, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=False)

    purchase_date = models.DateTimeField(default=timezone.now)
