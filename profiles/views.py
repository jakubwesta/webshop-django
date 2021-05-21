from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404

from .models import User
#from .forms import LoginForm

class UserHomeDetailsPageView(generic.DetailView):
    model = User
    template_name = 'profiles/user_page.html'

class LoginPageView(generic.FormView):
    #form_class = LoginForm
    template_name = 'profiles/login_page.html'
    success_url = '/product/2/'