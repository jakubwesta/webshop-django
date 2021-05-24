from django.urls.base import resolve
from products.models import Product
from django.shortcuts import get_object_or_404, resolve_url
from django.views import generic
from django.contrib.auth import views

from .models import User
from .forms import *
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from webshop import settings


class UserRegistrationView(generic.CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'profiles/user_registration_page.html'

    def get_success_url(self):
        return resolve_url('/user')

class UserLoginView(views.LoginView):
    model = User
    form_class = UserLoginForm
    template_name = 'profiles/user_login_page.html'

    def get_success_url(self):
        return resolve_url('/user')

class UserLogoutView(views.LogoutView):
    model = User
    next_page = settings.LOGOUT_REDIRECT_URL

class UserProductCreateView(generic.CreateView):
    model = Product
    template_name = 'profiles/user_product_create_page.html'
    form_class = ProductCreationForm

    def get_success_url(self):
        return resolve_url('/user')

class UserHomeDashobardView(generic.DetailView):
    model = User
    template_name = 'profiles/user_home_dashboard_page.html'

    def get_object(self):
        print("User primary key: " + str(self.request.user.pk))
        try:
            obj = User.objects.get(pk=self.request.user.pk)
        except:
            obj = None
        return obj
