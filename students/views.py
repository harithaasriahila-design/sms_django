from django.shortcuts import render
from .models import Student

def home(request):
    return render(request, 'students/index.html')

def student_login(request):
    error = None

    if request.method == "POST":
        roll_no = request.POST.get("roll_no")
        name = request.POST.get("name")

        try:
            student = Student.objects.get(roll_no=roll_no, name=name)
            return render(request, "students/dashboard.html", {"student": student})
        except Student.DoesNotExist:
            error = "Invalid Name or Roll Number"

    return render(request, "students/login.html", {"error": error})
