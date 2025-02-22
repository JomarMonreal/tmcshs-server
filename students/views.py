from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSerializer
from rest_framework.exceptions import PermissionDenied


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Users can only view their own student record.
        Superusers can view all records.
        """
        user = self.request.user
        if user.is_superuser:
            return Student.objects.all()
        return Student.objects.filter(user=user)

    def perform_update(self, serializer):
        """
        Allow users to update their own records only.
        Superusers can update any record.
        """
        user = self.request.user
        student = self.get_object()

        if not user.is_superuser and student.user != user:
            raise PermissionDenied(
                "You do not have permission to modify this student record.")

        serializer.save()

    def perform_destroy(self, instance):
        """
        Prevent users from deleting their own record.
        Only superusers can delete student records.
        """
        user = self.request.user
        if not user.is_superuser:
            raise PermissionDenied(
                "You do not have permission to delete this student record.")
        instance.delete()
