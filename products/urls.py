from django.urls import path
from . import views
  
urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('product/<uuid:uuid>/', views.ProductDetailsView.as_view(), name='product-details'),
    path('product/<uuid:uuid>/update/', views.ProductUpdateView.as_view(), name='product-update'),
]
