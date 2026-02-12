from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'student_class', 'parents_phone', 'fees_pending')
    search_fields = ('name', 'roll_no')
