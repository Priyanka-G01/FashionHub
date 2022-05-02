from django.urls import path
from . import views

urlpatterns=[
     path('become-customer/',views.become_customer,name='become_customer'),
    path('customer_det/',views.customer_det,name='customer_det'),
    path('edit_customer/',views.edit_customer,name='edit_customer'),
]