from django.urls import path
from . import views
  
urlpatterns = [
    path('purchase-details/<uuid:uuid>', views.PurchaseDetailsView.as_view(), name='purchase-details'),
    path('product/<uuid:product_uuid>/purchase/<uuid:uuid>/new-purchase-shipping', views.PurchaseShippingView.as_view(), name='new-purchase-shipping'),
    path('product/<uuid:product_uuid>/purchase/<uuid:uuid>/new-purchase-payment', views.PurchasePaymentView.as_view(), name='new-purchase-payment'),
]