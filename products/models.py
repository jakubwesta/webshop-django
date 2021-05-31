from django.db import models
from django.urls import reverse

import uuid
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from webshop import settings
from comments import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=70, blank=False)
    description = models.CharField(max_length=5000, blank=True)
    amount = models.IntegerField(blank=False, default=1)
    product_model = models.CharField(max_length=50, blank=True)
    manufacturer = models.CharField(max_length=50, blank=True)
    
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=False)

    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    comments = models.ManyToManyField(models.Comment, on_delete = models.CASCADE, blank=True, null=True)
 
    publicly_listed = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("product-details", kwargs={"uuid": self.pk})

    def get_update_url(self):
        return reverse("product-update", kwargs={"uuid": self.pk})

        