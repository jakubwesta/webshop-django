from django.urls import path
from . import views
  
urlpatterns = [
    path('user-me/', views.UserDashobardHomeView.as_view(), name='user-dashboard-home'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('user/<str:username>/', views.UserPublicView.as_view(), name='user-public'),
    path('user-me/create-product/', views.UserProductCreateView.as_view(), name='create-product'),
    path('user-me/selling-products/', views.UserDashboardSellingProductsView.as_view(), name='user-dashboard-selling-products'),
    path('user-me/bought-products/', views.UserDashboardBoughtProductsView.as_view(), name='user-dashboard-bought-products')
]