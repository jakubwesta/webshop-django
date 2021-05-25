from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    AVAIBLE_STARS = [
        (1, 'Very bad'),
        (2, 'Bad'),
        (3, 'Nothing special'),
        (4, 'Good'),
        (5, 'Very good')
    ]
    name = models.CharField(max_length=70, blank=False)
    description = models.CharField(max_length=5000, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    buy_now = models.DecimalField(decimal_places=2, max_digits=8, blank=False)
    auction_starting_price = models.DecimalField(decimal_places=2, max_digits=8, blank=True)
    amount = models.IntegerField(blank=False, default=1)
    manufacturer = models.CharField(max_length=50, blank=True)
    product_model = models.CharField(max_length=50, blank=True)
    customers_review = models.DecimalField(validators=[MinValueValidator(1), MaxValueValidator(5)], decimal_places=2, max_digits=3, null=True)
    customers_rating = models.IntegerField(choices=AVAIBLE_STARS, default=5)
    publicly_listed = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    def buy(self, buyer, amount, price):
        self.amount -= int(amount)
        self.save()
        buyer.money_spent += float(price)
        buyer.save()

    def get_absolute_url(self):
        return reverse("product-details", kwargs={"pk": self.pk})

