from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model

from random import randint


def get_random_email(chars):
    email_temp = str(
        get_random_string(length=int(chars), allowed_chars='abcdefghijklmnoprstuowjxyz1234567890') + '@gmail.com')
    return email_temp


class Command(BaseCommand):
    help = 'Create random user(s)'
    User = get_user_model()

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, nargs='?', help='Number of users to create')

    def generate_random_user(self):
        user_key = randint(0, 1000000)
        email = str(get_random_email(8))
        password = str('Password' + str(user_key))
        user = self.User.objects.create_user(username=str('User_' + str(user_key)),
                                             email=email,
                                             password=password)
        user.first_name = str('FirstName_' + str(user_key))
        user.last_name = str('LastName_' + str(user_key))
        user.save()
        self.stdout.write(f"Created User  ->  email: {email} | password: {password} -> ", ending='')
        self.stdout.write(self.style.SUCCESS("OK"))

    def handle(self, *args, **kwargs):
        if kwargs['amount'] and kwargs['amount'] > 1:
            for _ in range(kwargs['amount']):
                self.generate_random_user()
            self.stdout.write(self.style.SUCCESS(f"Successfully created {kwargs['amount']} users."))
        else:
            self.generate_random_user()
            self.stdout.write(self.style.SUCCESS(f"Successfully created user."))
