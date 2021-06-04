from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, resolve_url
from django.views import generic

from purchases.models import Purchase, Cart
from .forms import *

from webshop import settings


class UserRegistrationView(generic.CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'profiles/user_registration_page.html'

    def get_success_url(self):
        return resolve_url('/user-me')


class UserLoginView(views.LoginView):
    model = User
    form_class = UserLoginForm
    template_name = 'profiles/user_login_page.html'

    def get_success_url(self):
        return resolve_url('/user-me')


class UserLogoutView(LoginRequiredMixin, views.LogoutView):
    model = User
    next_page = settings.LOGOUT_REDIRECT_URL


class UserPublicView(generic.DetailView):
    model = User
    template_name = 'profiles/user_public_page.html'

    def get_object(self):
        obj = get_object_or_404(User, username=self.kwargs['username'])
        return obj

    def get_context_data(self, **kwargs):
        context = super(UserPublicView, self).get_context_data(**kwargs)
        return context


class UserProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    template_name = 'profiles/user_product_create_page.html'
    form_class = ProductCreationForm

    def get_success_url(self):
        return resolve_url('/user-me')

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class UserDashobardHomeView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'profiles/user_dashboard_home_page.html'

    def get_object(self):
        obj = get_object_or_404(User, pk=self.request.user.pk)
        return obj


class UserDashboardSellingProductsView(LoginRequiredMixin, generic.ListView):
    model = User
    context_object_name = 'selling_list'
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


class UserDashboardSoldProductsView(LoginRequiredMixin, generic.ListView):
    model = User
    context_object_name = 'sold_list'
    template_name = 'profiles/user_dashboard_sold_products_page.html'

    def get_ordering(self):
        if self.request.GET.get('ordering'):
            ordering = str(self.request.GET['ordering'])
        else:
            ordering = '-purchase_date'
        return ordering

    def get_queryset(self):
        queryset = Purchase.objects.filter(product__seller=self.request.user)
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


class UserCartView(LoginRequiredMixin, generic.ListView):
    model = User
    context_object_name = 'cart_list'
    template_name = 'profiles/user_cart_page.html'

    def get_ordering(self):
        if self.request.GET.get('ordering'):
            ordering = str(self.request.GET['ordering'])
        else:
            ordering = '-addition_date'
        return ordering

    def get_queryset(self):
        queryset = Cart.objects.filter(user=self.request.user)
        queryset = queryset.order_by(self.get_ordering())
        return queryset
