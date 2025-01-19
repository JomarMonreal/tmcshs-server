# views.py
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from .permissions import IsSuperAdminForNonGetMethods


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsSuperAdminForNonGetMethods]
