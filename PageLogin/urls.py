from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginPage, name='Login'),
    path('logout/', logoutPage, name='Logout'),
    path('register/', register, name="Register"),
    path('registerCard/<str:usuario>/', RegisterCard.as_view(), name="RegisterCard"),
]