from django.urls import path
from . import views
  
urlpatterns = [
    path('user/', views.UserHomeDashobardView.as_view(), name='user-dashboard-home'),
    path('user/register/', views.UserRegistrationView.as_view(), name='register'),
    path('user/login/', views.UserLoginView.as_view(), name='login'),
    path('user/logout/', views.UserLogoutView.as_view(), name='logout'),
    path('user/create-product/', views.UserProductCreateView.as_view(), name='create-product'),
]