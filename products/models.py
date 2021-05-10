from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=70, blank=False)
    buy_now = models.DecimalField(decimal_places=2, max_digits=8, blank=False)
    auction_starting_price = models.DecimalField(decimal_places=2, max_digits=8, blank=True)
    #amount = models.IntegerField(blank=False)
    #rating = models.DecimalField(blank=True, decimal_places=1, ma)
        
    
