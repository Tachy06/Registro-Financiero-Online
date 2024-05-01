from django.urls import path
from .views import *

urlpatterns = [
    path('admin666/', panelAdmin.as_view(), name='Panel_Admin'),
    path('deleteUser/<int:usuario_id>/', DeleteUser.as_view(), name='Delete_User'),
    path('createUserAdmin/', CreateUser.as_view(), name='Create_User'),
    path('viewCards/', ViewCards.as_view(), name='View_Cards'),
    path('addCardAdmin/', AddCard.as_view(), name='Add_Card'),
    path('modifiedUser/<int:usuario_id>/', modifiedUser.as_view(), name='Modified_User'),
]