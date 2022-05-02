from unicodedata import name
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('become-designer/',views.become_designer,name='become_designer'),
    path('designer-admin/',views.designer_admin,name='designer_admin'),
    path('add-product/',views.add_product, name='add_product'),
    path('edit-designer/',views.edit_designer,name='edit_designer'),
    path('designers/',views.designers,name='designers'),
    path('<int:designer_id>/',views.designer,name='designer'),

    
]