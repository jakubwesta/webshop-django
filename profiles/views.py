from purchases.models import Purchase
from django.db.models import query
from django.http import request
from django.urls.base import resolve
from products.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
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

class UserLogoutView(LoginRequiredMixin, views.LogoutView):
    model = User
    next_page = settings.LOGOUT_REDIRECT_URL

class UserProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    template_name = 'profiles/user_product_create_page.html'
    form_class = ProductCreationForm

    def get_success_url(self):
        return resolve_url('/user')

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

class UserDashobardHomeView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'profiles/user_dashboard_home_page.html'

    def get_object(self):
        try:
            obj = User.objects.get(pk=self.request.user.pk)
        except:
            obj = None
        return obj

class UserDashboardSellingProductsView(LoginRequiredMixin, generic.ListView):
    model = User
    context_object_name = 'product_list'
    template_name = 'profiles/user_dashboard_selling_products_page.html'
    
    def get_ordering(self):
        if self.request.GET.get('ordering'):
            ordering = str(self.request.GET['ordering'])
        else:
            ordering = '-creation_date'
        return ordering

    def get_queryset(self):
        queryset = Product.objects.filter(seller=self.request.user)
        queryset = queryset.order_by(self.get_ordering())
        return queryset

class UserDashboardBoughtProductsView(LoginRequiredMixin, generic.ListView):
    model = User
    context_object_name = 'purchases_list'
    template_name = 'profiles/user_dashboard_bought_products_page.html'
    
    def get_ordering(self):
        if self.request.GET.get('ordering'):
            ordering = str(self.request.GET['ordering'])
        else:
            ordering = '-purchase_date'
        return ordering

    def get_queryset(self):
        queryset = Purchase.objects.filter(buyer=self.request.user)
        queryset = queryset.order_by(self.get_ordering())
        return queryset
