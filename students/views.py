from urllib import request

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
import csv

from .models import Student, Staff
from .forms import StudentForm


# ---------------- HOME PAGE ----------------
def home(request):
    return render(request, "students/index.html")


# ---------------- STUDENT LOGIN ----------------
def student_login(request):

    if request.method == "POST":
        roll_no = request.POST.get("roll_no")

        try:
            student = Student.objects.get(roll_no=roll_no)
            request.session["student_id"] = student.id
            return redirect("dashboard")

        except Student.DoesNotExist:
            messages.error(request, "Invalid Roll Number")

    return render(request, "students/student_login.html")


# ---------------- STUDENT DASHBOARD ----------------
def dashboard(request):

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("student_login")

    student = Student.objects.get(id=student_id)

    return render(request, "students/dashboard.html", {"student": student})


# ---------------- STAFF LOGIN ----------------
def staff_login(request):

    if request.method == "POST":
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        try:
            staff = Staff.objects.get(email=email, phone=phone)
            request.session["staff_id"] = staff.id
            return redirect("staff_dashboard")

        except Staff.DoesNotExist:
            messages.error(request, "Invalid Email or Phone")

    return render(request, "students/staff_login.html")


# ---------------- STAFF DASHBOARD ----------------
def staff_dashboard(request):

    if "staff_id" not in request.session:
        return redirect("staff_login")

    students = Student.objects.all()

    return render(request, "students/staff_dashboard.html", {"students": students})


# ---------------- ADD STUDENT ----------------
def add_student(request):

    if "staff_id" not in request.session:
        return redirect("staff_login")

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("staff_dashboard")

    else:
        form = StudentForm()

    return render(request, "students/add_student.html", {"form": form})


# ---------------- EDIT STUDENT ----------------
def edit_student(request, id):

    if "staff_id" not in request.session:
        return redirect("staff_login")

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":

        student.name = request.POST.get("name")
        student.roll_no = request.POST.get("roll_no")
        student.student_class = request.POST.get("student_class")
        student.age = request.POST.get("age")
        student.gender = request.POST.get("gender")
        student.blood_group = request.POST.get("blood_group")
        student.address = request.POST.get("address")
        student.parents_phone = request.POST.get("parents_phone")
        student.exam_marks = request.POST.get("exam_marks")
        student.attendance = request.POST.get("attendance")
        student.total_fees = request.POST.get("total_fees")
        student.fees_paid = request.POST.get("fees_paid")

        if student.total_fees and student.fees_paid:
            student.fees_pending = int(student.total_fees) - int(student.fees_paid)

        student.save()

        return redirect("staff_dashboard")

    return render(request, "students/edit_student.html", {"student": student})


# ---------------- DELETE STUDENT ----------------
def delete_student(request, id):

    if "staff_id" not in request.session:
        return redirect("staff_login")

    student = get_object_or_404(Student, id=id)
    student.delete()

    return redirect("staff_dashboard")


# ---------------- DOWNLOAD CSV ----------------
def download_students(request):

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)
    writer.writerow(["ID", "Name", "Roll No"])

    students = Student.objects.all()

    for student in students:
        writer.writerow([student.id, student.name, student.roll_no])

    return response


# ---------------- STUDENT LOGOUT ----------------
def student_logout(request):
    request.session.flush()
    return redirect("student_login")


# ---------------- STAFF LOGOUT ----------------
def staff_logout(request):
    request.session.flush()
    return redirect("staff_login")

from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


def update_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.roll_no = request.POST.get("roll_no")
        student.student_class = request.POST.get("student_class")
        student.age = request.POST.get("age")
        student.gender = request.POST.get("gender")
        student.blood_group = request.POST.get("blood_group")
        student.address = request.POST.get("address")
        student.parents_phone = request.POST.get("parents_phone")
        student.exam_marks = request.POST.get("exam_marks")
        student.attendance = request.POST.get("attendance")
        student.total_fees = request.POST.get("total_fees")
        student.fees_paid = request.POST.get("fees_paid")

        student.fees_pending = int(student.total_fees) - int(student.fees_paid)

        student.save()

        return redirect('staff_dashboard')

    return render(request, "students/edit_student.html", {"student": student})

from django.shortcuts import render, redirect
from .models import Student  # உங்கள் student model
from django.contrib import messages

def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        roll_no = request.POST.get('roll_no')

        try:
            student = Student.objects.get(name=name, roll_no=roll_no)
            request.session['student_id'] = student.id
            return redirect('student_dashboard')  # student dashboard URL
        except Student.DoesNotExist:
            return render(request, "students/login.html", {'error': "Invalid Name or Roll No"})

    return render(request, "students/login.html")

def student_login(request):
    return render(request, "students/login.html")

def student_dashboard(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')

    student = Student.objects.get(id=student_id)
    return render(request, "students/dashboard.html", {'student': student})

def student_dashboard(request):
    return render(request, "students/dashboard.html", {'student': student})

    from django.shortcuts import render, redirect
from .models import Student

def student_login(request):
    error = None
    if request.method == "POST":
        name = request.POST.get("name").strip()
        roll_no = request.POST.get("roll_no").strip()
        
        try:
            student = Student.objects.get(name__iexact=name, roll_no__iexact=roll_no)
            # store student info in session
            request.session['student_id'] = student.id
            return redirect('student_dashboard')  # make sure you have this URL
        except Student.DoesNotExist:
            error = "Invalid name or roll number"

    return render(request, "students/login.html", {"error": error})

    # students/views.py
from django.shortcuts import render

def student_dashboard(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')  # redirect if not logged in

    # fetch student info to display on dashboard
    from .models import Student
    student = Student.objects.get(id=student_id)

    return render(request, 'students/dashboard.html', {'student': student})

# students/views.py
def student_dashboard(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')
    student = Student.objects.get(id=student_id)
    return render(request, 'students/dashboard.html', {'student': student})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


def update_student(request, id):
    
    # Get student object using ID
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        
        # Get data from form
        student.name = request.POST.get('name')
        student.roll_no = request.POST.get('roll_no')
        student.student_class = request.POST.get('student_class')
        student.gender = request.POST.get('gender')
        student.blood_group = request.POST.get('blood_group')
        student.address = request.POST.get('address')
        student.parents_phone = request.POST.get('parents_phone')

        # Safe integer conversion
        def safe_int(value):
            try:
                return int(value)
            except:
                return 0

        student.age = safe_int(request.POST.get('age'))
        student.exam_marks = safe_int(request.POST.get('exam_marks'))
        student.attendance = safe_int(request.POST.get('attendance'))
        student.total_fees = safe_int(request.POST.get('total_fees'))
        student.fees_paid = safe_int(request.POST.get('fees_paid'))

        # Calculate pending fees
        student.fees_pending = student.total_fees - student.fees_paid

        # Save updated student
        student.save()

        return redirect('staff_dashboard')

    else:
        form = StudentForm(instance=student)

    return render(request, 'students/edit_student.html', {
        'form': form,
        'student': student
    })   

from django.shortcuts import redirect, get_object_or_404
from .models import Student

def pay_fees(request, id):
    student = get_object_or_404(Student, id=id)
    student.fees_status = "Paid"
    student.save()
    return redirect('staff_dashboard')

