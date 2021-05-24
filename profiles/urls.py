from django.urls import path
from django.urls import include
from . import views
  
urlpatterns = [
    path('user/register/', views.UserRegistrationView.as_view(), name='register'),
    path('user/login/', views.UserLoginView.as_view(), name='login'),
    path('user/logout/', views.UserLogoutView.as_view(), name='logout'),
    path('user/', views.UserHomeDashobardPageView.as_view(), name='user dashboard home'),
]