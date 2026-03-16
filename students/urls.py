from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path("student_login/", views.student_login, name="student_login"),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),  # 🔹 must match exactly
    path("staff_login/", views.staff_login, name="staff_login"),
    path("staff_dashboard/", views.staff_dashboard, name="staff_dashboard"),
      
    path("add_student/", views.add_student, name="add_student"),
    path("edit_student/<int:id>/", views.edit_student, name="edit_student"),
    path("delete_student/<int:id>/", views.delete_student, name="delete_student"),
    path('update_student/<int:id>/', views.update_student, name='update_student'),


    path("download_students/", views.download_students, name="download_students"),

    path("student_logout/", views.student_logout, name="student_logout"),
    path("staff_logout/", views.staff_logout, name="staff_logout"),

]


