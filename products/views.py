from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Product

class ProductPageView(generic.DetailView):
    model = Product
    template_name = 'products/product_page.html'
    
    '''
    product=Product.objects.get(id=id)
    def post(self, request):
        pass
    '''
