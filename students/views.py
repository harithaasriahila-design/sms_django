from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Staff
from .forms import StudentForm


# ---------------- HOME PAGE ----------------
def home(request):
    return render(request, 'students/index.html')


# ---------------- STUDENT LOGIN ----------------
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


# ---------------- STAFF LOGIN ----------------
def staff_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        try:
            staff = Staff.objects.get(email=email, phone=phone)
            request.session['staff_id'] = staff.id
            return redirect('staff_dashboard')   # IMPORTANT
        except Staff.DoesNotExist:
            return render(request, 'students/staff_login.html', {
                'error': 'Invalid Email or Phone'
            })

    return render(request, 'students/staff_login.html')

# ---------------- STAFF DASHBOARD ----------------
def staff_dashboard(request):
    if 'staff_id' not in request.session:
        return redirect('staff_login')

    students = Student.objects.all()
    return render(request, 'students/staff_dashboard.html', {'students': students})


# ---------------- ADD STUDENT ----------------
def add_student(request):
    if 'staff_id' not in request.session:
        return redirect('staff_login')

    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('staff_dashboard')

    return render(request, 'students/add_student.html', {'form': form})


# ---------------- UPDATE STUDENT ----------------
def update_student(request, id):
    if 'staff_id' not in request.session:
        return redirect('staff_login')

    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('staff_dashboard')

    return render(request, 'students/update_student.html', {'form': form})


# ---------------- DELETE STUDENT ----------------
def delete_student(request, id):
    if 'staff_id' not in request.session:
        return redirect('staff_login')

    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('staff_dashboard')