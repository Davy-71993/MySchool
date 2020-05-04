from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admindashboard/', views.admindashboard, name='admindashboard'),
    path('calender/create/', views.create_calendar, name='create_calender'), 
    path('calender/setup/', views.setup_calendar, name='setup_calendar'),
    path('calender/', views.calendar, name='calendar'),
    
    path('login/', views.login_user, name='login' ),
    path('logout/', views.signout, name='logout'),
    path('signup/', views.signup, name='signup' ),

    path('subjects/', views.subjects, name='subjects'),
    path('updatesubject/<pk>/', views.update_subject, name='update_subject'),
    path('deletesubject/<pk>/', views.delete_subject, name='delete_subject'),

    path('addpaper/<pk>/<px>', views.add_paper, name='add_paper'),
    path('editpaper/<pk>/', views.edit_paper, name='edit_paper'),
    path('deletepaper/<pk>/', views.delete_paper, name='delete_paper'),
]
