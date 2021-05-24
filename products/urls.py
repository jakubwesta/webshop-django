from django.urls import path
from . import views
  
urlpatterns = [
    path('product/<int:pk>/', views.ProductDetailsView.as_view(), name='product-details'),
    path('', views.ProductListView.as_view(), name='home'),
]