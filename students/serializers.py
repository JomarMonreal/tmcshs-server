from rest_framework import serializers
from .models import Student
from enrollments.serializers import EnrollmentSerializer


class StudentSerializer(serializers.ModelSerializer):
    enrollments = EnrollmentSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = '__all__'
