from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Product

class ProductDetailsView(generic.DetailView):
    model = Product
    template_name = 'products/product_page.html'
    
    def get_object(self):
        print("Product primary key: " + str(self.kwargs['pk']))
        try:
            obj = Product.objects.get(pk=self.kwargs['pk'])
        except:
            obj = None
        return obj

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
