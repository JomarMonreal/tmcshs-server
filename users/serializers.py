from django.contrib.auth.models import User
from rest_framework import serializers
from django.db import transaction

from students.models import Student


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    # Student Fields
    student_number = serializers.IntegerField(required=False)
    first_name = serializers.CharField(max_length=255)
    middle_name = serializers.CharField(max_length=255, required=False,
                                        allow_null=True, allow_blank=True)
    last_name = serializers.CharField(max_length=255)
    birth_date = serializers.DateField()
    address = serializers.CharField()
    contact_number = serializers.CharField(max_length=15)
    guardian_name = serializers.CharField(max_length=255)
    guardian_contact = serializers.CharField(max_length=15)
    is_enrolled = serializers.BooleanField(default=False)
    academic_year = serializers.IntegerField(required=False)
    grade_level = serializers.IntegerField(required=False)
    stepsTaken = serializers.IntegerField(default=0)
    profile_pic = serializers.CharField(max_length=1024, required=False,
                                        allow_null=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password',
                  'student_number', 'first_name', 'middle_name',
                  'last_name', 'birth_date', 'address', 'contact_number',
                  'guardian_name', 'guardian_contact', 'is_enrolled',
                  'academic_year', 'grade_level', 'stepsTaken',
                  'profile_pic',]

    def create(self, validated_data):
        student_data = {
            key: validated_data.pop(key) for key in [
                'first_name', 'last_name',
                'birth_date', 'address', 'contact_number', 'guardian_name',
                'guardian_contact', 'is_enrolled', 'stepsTaken', 'profile_pic',
            ]
        }

        with transaction.atomic():
            # Create User
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password']
            )

            # Link Student to User
            Student.objects.create(user=user, email=user.email, **student_data)

        return user
