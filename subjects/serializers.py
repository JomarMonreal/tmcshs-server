from rest_framework import serializers
from .models import Subject
from enrollments.serializers import EnrollmentSerializer


class SubjectSerializer(serializers.ModelSerializer):
    enrollments = EnrollmentSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = '__all__'
