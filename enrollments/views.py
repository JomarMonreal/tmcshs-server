from rest_framework import viewsets
from .models import Enrollment
from .serializers import EnrollmentSerializer
from .permissions import IsSuperAdminForNonGetMethods


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsSuperAdminForNonGetMethods]
