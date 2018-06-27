from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.personal, name = 'personal'),
    path(r'contact/', views.contact, name = 'contact')
]
