from django import forms
from .models import Student, Staff

# Student Form
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # எந்த fields form-ல் include பண்ணலாம்
        fields = [
            'name', 'roll_no', 'student_class', 'age',
            'gender', 'blood_group', 'address', 'parents_phone',
            'exam_marks', 'attendance', 'total_fees', 'fees_paid', 'fees_pending'
        ]
        # Optional: field label customize பண்ணலாம்
        labels = {
            'roll_no': 'Roll Number',
            'student_class': 'Class',
            'parents_phone': "Parent's Phone",
        }
        # Optional: form widgets customize பண்ணலாம்
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'gender': forms.Select(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]),
            'blood_group': forms.Select(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), 
                                                 ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'),
                                                 ('AB+', 'AB+'), ('AB-', 'AB-')]),
        }

# Staff Form
class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'email', 'phone']