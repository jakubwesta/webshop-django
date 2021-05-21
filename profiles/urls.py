from django.urls import path
from django.urls import include
from . import views
  
urlpatterns = [
    path('user/<int:pk>/', views.UserHomeDetailsPageView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('user/login/', views.LoginPageView.as_view()),
]