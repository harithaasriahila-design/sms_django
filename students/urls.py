from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student-login/', views.student_login, name='student_login'),
    
]
