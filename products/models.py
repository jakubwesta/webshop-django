from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from webshop import settings

class Product(models.Model):
    name = models.CharField(max_length=70, blank=False)
    description = models.CharField(max_length=5000, blank=True)
    amount = models.IntegerField(blank=False, default=1)
    product_model = models.CharField(max_length=50, blank=True)
    manufacturer = models.CharField(max_length=50, blank=True)
    
    buy_now = models.DecimalField(decimal_places=2, max_digits=10, blank=False)
    auction_starting_price = models.DecimalField(decimal_places=2, max_digits=10, blank=True)

    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='seller_user')
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True, null=True, default=None, related_name='buyer_user')
 
    publicly_listed = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("product-details", kwargs={"pk": self.pk})

    def buy(self, buyer, amount, price):
        self.amount -= int(amount)
        self.save()
        buyer.money_spent += float(price)
        buyer.save()

