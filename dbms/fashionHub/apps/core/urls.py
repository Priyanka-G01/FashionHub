import imp
from django.urls import path
from . import views


urlpatterns = [
    path('',views.frontpage,name='frontpage'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.register,name='register'),
    path('customer_register/',views.customer_register.as_view(),name='customer_register'),
    path('designer_register/',views.designer_register.as_view(),name='designer_register'),
    path('login/',views.login_request, name='login'),
    path('logout/',views.logout_view, name='logout'),
]
