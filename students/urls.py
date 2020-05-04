from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.students, name='students' ),
    path('register/', views.add, name='register_student'),
    path('import/', views.import_students, name='import_students'),
    path('details/<pk>/', views.student, name='student'),
    path('delete/<pk>/', views.delete_student, name='delete_student'),

    path('house/<hs>/', views.view_by_house, name='students_by_house'),
    path('<cl>/', views.view_by_class, name='students_by_class'),
    path('<cl>/<strm>/', views.view_by_stream, name='students_by_stream'),
]
