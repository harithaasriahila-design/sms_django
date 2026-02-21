from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    student_class = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    address = models.TextField()
    parents_phone = models.CharField(max_length=15)

    exam_marks = models.IntegerField(default=0)
    attendance = models.IntegerField(default=0)

    total_fees = models.IntegerField(default=0)
    fees_paid = models.IntegerField(default=0)
    fees_pending = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"
from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    