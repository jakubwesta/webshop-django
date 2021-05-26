from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from products.forms import BuynowForm
from django.shortcuts import redirect, render, resolve_url
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse
from django.shortcuts import get_object_or_404

from .models import Product
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from purchases.models import Purchase

class ProductDetailsView(generic.DetailView):
    model = Product
    template_name = 'products/product_page.html'
    
    def get_object(self):
        try:
            obj = Product.objects.get(pk=self.kwargs['uuid'])
        except:
            obj = None
        return obj

    def post(self, request, *args, **kwargs):
        if 'buy_now' in request.POST:
            buy_now_form = BuynowForm(request.POST)
            if buy_now_form.is_valid():
                obj = self.get_object()
                obj.amount -= 1
                obj.save()
                Purchase.objects.create(product=obj,
                                        buyer=self.request.user,
                                        amount=1,
                                        price=obj.buy_now)
                return redirect('product-details', uuid=self.kwargs['uuid'])

class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'products/products_list_page.html'

    def get_ordering(self):
        if self.request.GET.get('ordering'):
            ordering = str(self.request.GET['ordering'])
        else:
            ordering = '-creation_date'
        return ordering
    
    def get_queryset(self):
        queryset = Product.objects.all()
        queryset = queryset.order_by(self.get_ordering())
        return queryset
