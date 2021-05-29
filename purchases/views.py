from django.http import request
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django import views
from django.urls import reverse

from .models import Payment, Purchase, Shipping
from .forms import PurchasePaymentForm, PurchaseShippingForm


class PurchaseDetailsView(LoginRequiredMixin, generic.DetailView):
    model = Purchase
    template_name = 'purchases/purchase_details_page.html'

    def get_object(self):
        obj = get_object_or_404(Purchase, pk=self.kwargs['uuid'])
        if self.request.user in obj.get_accessible_for_list():
            return obj
        else:
            raise Http404('You are not buyer/seller of the product!')

        
class PurchaseShippingView(LoginRequiredMixin, generic.CreateView):
    model = Shipping
    template_name = 'purchases/purchase_new_shipping_page.html'
    form_class = PurchaseShippingForm

    def get_success_url(self):
        return reverse("new-purchase-payment", kwargs={"uuid": self.kwargs['uuid'], 'product_uuid': self.kwargs['product_uuid']})


class PurchasePaymentView(LoginRequiredMixin, generic.CreateView):
    model = Shipping
    template_name = 'purchases/purchase_new_payment_page.html'
    form_class = PurchasePaymentForm

    def get_full_model(self):
        obj = get_object_or_404(Purchase, pk=self.kwargs['uuid'])
        return obj

    def get_object(self):
        obj = get_object_or_404(Payment, pk=self.kwargs['uuid'])
        return obj

    def get_shipping_model(self):
        obj = get_object_or_404(Shipping, pk=self.kwargs['uuid'])
        return obj

    def get_success_url(self):
        purchase_obj = self.get_full_model()
        purchase_obj.shipping = self.get_shipping_model()
        purchase_obj.payment = self.get_object()
        purchase_obj.finished = True
        purchase_obj.save()
        product_obj = self.get_full_model().product
        product_obj.amount -= int(self.get_full_model().amount)
        if product_obj.amount == 0:
            product_obj.publicly_listed = False
        product_obj.save()
        return self.get_full_model().get_absolute_url()

