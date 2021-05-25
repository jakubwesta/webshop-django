from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model

from random import randint
import decimal
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from products.models import Product


def get_random_email(chars):
    email_temp = str(get_random_string(length=int(chars), allowed_chars='abcdefghijklmnoprstuowjxyz1234567890') + '@gmail.com')
    return email_temp

class Command(BaseCommand):
    help = 'Creates random product(s)'
    User = get_user_model()

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, nargs='?', help='Number of products to create')

    def generate_random_seller_user(self):
        user_key = randint(0, 1000000)
        email = str(get_random_email(8))
        password = str('Password' + str(user_key))
        self.user = self.User.objects.create_user(username=str('User_' + str(user_key)),
                                             email=email,
                                             password=password)
        self.user.first_name = str('FirstName_' + str(user_key))
        self.user.last_name = str('LastName_' + str(user_key))
        self.user.save()
        self.stdout.write(f"Created seller (User) of the products  ->  email: {email} | password: {password}")

    def generate_random_product(self):
        product_key = randint(0, 1000000)
        price = float(decimal.Decimal(product_key))
        Product.objects.create(name=str('Product_' + str(product_key)),
                               description=str('Description_' + str(product_key)),
                               amount=int(product_key),
                               product_model=str('Model_' + str(product_key)),
                               manufacturer=str('Manufacturer_' + str(product_key)),
                               buy_now=float(price),
                               auction_starting_price=float(price - 0.01),
                               seller=self.user)

    def handle(self, *args, **kwargs):
        self.generate_random_seller_user()
        if kwargs['amount'] and kwargs['amount'] > 1:
            for _ in range(kwargs['amount']):
                self.generate_random_product()
            self.stdout.write(f"Succesfully created {kwargs['amount']} products.")
        else:
            self.generate_random_product()
            self.stdout.write(f"Succesfully created product.")

