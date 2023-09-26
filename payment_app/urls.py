from django.urls import path
from . import views 

urlpatterns = [
    path('payments/', views.create_payment, name= "create_payment"),
    path('payments/<int:payment_id>/', views.get_payment_details, name="get_payment_details"),
]
