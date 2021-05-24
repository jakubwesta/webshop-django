from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import fields
from django.http import HttpResponse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls.base import reverse
from django import forms

from .models import User
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from products.models import Product


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register'))

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Login'))
        
class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'buy_now', 'auction_starting_price',
                'amount', 'manufacturer', 'product_model')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Create product'))




