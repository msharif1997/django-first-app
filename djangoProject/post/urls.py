from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.index, name = 'index'),
#    path(r'details/(?P<id>\d+/)/$', views.details, name = 'details')
    path(r'details/<int:id>/', views.details, name = 'details')
]
