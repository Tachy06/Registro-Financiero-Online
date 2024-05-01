from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('profile/', viewProfile.as_view(), name='Profile'),
    path('change_password/', ChangePassword.as_view(), name='Change_Password'),
]