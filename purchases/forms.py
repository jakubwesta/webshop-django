from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import Shipping, Payment


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
        self.helper.add_input(Submit('submit', 'Continue to payment'))
