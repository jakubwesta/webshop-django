from django.urls import path
from . import views
  
urlpatterns = [
    path('purchase-details/<uuid:uuid>', views.PurchaseDetailsView.as_view(), name='purchase-details'),
    path('purchase/<uuid:uuid>/new-purchase-shipping', views.PurchaseDetailsView.as_view(), name='new-purchase-shipping'),
    path('purchase/<uuid:uuid>/new-purchase-payment', views.PurchaseDetailsView.as_view(), name='new-purchase-payment'),
]