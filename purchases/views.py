from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django import views

from .models import Purchase


class PurchaseDetailsView(LoginRequiredMixin, generic.DetailView):
    model = Purchase
    template_name = 'purchases/purchase_details_page.html'

    def get_object(self):
        obj = get_object_or_404(Purchase, pk=self.kwargs['uuid'])
        return obj
        
