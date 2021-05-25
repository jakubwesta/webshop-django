from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import fields
from django.http import HttpResponse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls.base import reverse
from django import forms

from .models import Product
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from products.models import Product

class BuynowForm(forms.Form):
    buy_now = forms.CharField()