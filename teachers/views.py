from rest_framework import viewsets
from .permissions import IsSuperAdminForNonGetMethods
from .models import Teacher
from .serializers import TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsSuperAdminForNonGetMethods]
