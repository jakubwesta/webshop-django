from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import fields
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls.base import reverse
from django import forms

from .models import Shipping, Payment
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class PurchaseShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = ('email', 'country', 'city', 'zip_code', 'home_address', 'name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Login'))


class PurchasePaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('card_number', 'card_expiry_date', 'card_security_number', 'card_owner_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Login'))
