from rest_framework import viewsets
from .permissions import IsSuperAdminForNonGetMethods
from .models import Subject
from .serializers import SubjectSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsSuperAdminForNonGetMethods]
