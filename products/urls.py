from django.urls import path
from . import views
  
urlpatterns = [
    path('product/<int:pk>/', views.ProductPageView.as_view()),
]