from rest_framework import serializers
from .models import Enrollment
from students.models import Student
from subjects.models import Subject


class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all())
    subject = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all())

    class Meta:
        model = Enrollment
        fields = '__all__'
