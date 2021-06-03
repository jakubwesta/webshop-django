from django.db import models
from django.urls import reverse

import uuid
import os, sys
from decimal import *
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from webshop import settings
from comments.models import Comment

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=70, blank=False)
    description = models.CharField(max_length=5000, blank=True)
    amount = models.IntegerField(blank=False, default=1)
    product_model = models.CharField(max_length=50, blank=True)
    manufacturer = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=False)

    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    comments = models.ManyToManyField(Comment, blank=True)
    rating = models.DecimalField(blank=True, null=True, default=None, decimal_places=1)
    rating_votes = models.IntegerField(blank=True, null=True, default=0)
 
    publicly_listed = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    @property
    def rating(self):
        try:
            rating = 0
            iteration = 0
            for comment in self.comments.all():
                rating += int(comment.stars)
                iteration += 1
            rating = Decimal(rating / iteration)
            return round(rating, 1)
        except:
            return round(Decimal(0 / 1), 1)

    @property
    def rating_votes(self):
        return int(len(self.comments.all()))

    def get_absolute_url(self):
        return reverse("product-details", kwargs={"uuid": self.pk})

    def get_update_url(self):
        return reverse("product-update", kwargs={"uuid": self.pk})

        