from django.urls import path
from . import views 

urlpatterns = [
    path('create_settlements/', views.create_settlements, name = "create_settlements"),
    path('retrieve_settlement/<str:settlement_id>/', views.retrieve_settlement, name = "retrieve_settlement"),
]
