from django.urls import path
from . import views
  
urlpatterns = [
    path('purchase/<uuid:uuid>', views.PurchaseDetailsView.as_view(), name='purchase-details'),
]