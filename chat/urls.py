
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='super_admin'),
    path('<str:room_name>/', views.room, name='room'),
    
]
