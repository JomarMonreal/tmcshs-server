from django.db import models
from enrollments.models import Enrollment
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name="student", primary_key=True)
    student_number = models.PositiveBigIntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    guardian_name = models.CharField(max_length=255)
    guardian_contact = models.CharField(max_length=15)
    is_enrolled = models.BooleanField(default=False)
    academic_year = models.PositiveIntegerField(blank=True, null=True)
    grade_level = models.PositiveIntegerField(blank=True, null=True)
    enrollments = models.ManyToManyField(Enrollment,
                                         related_name='students', blank=True)
    stepsTaken = models.PositiveIntegerField(default=0)
    profile_pic = models.CharField(max_length=1024, blank=True, null=True)
    documents = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
