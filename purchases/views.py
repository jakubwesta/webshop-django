from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django import views

from .models import Purchase


class PurchaseDetailsView(LoginRequiredMixin, generic.DetailView):
    model = Purchase
    template_name = 'purchases/purchase_details_page.html'

    def get_object(self):
        try:
            obj = Purchase.objects.get(pk=self.kwargs['uuid'])
        except:
            obj = None
        return obj
        
