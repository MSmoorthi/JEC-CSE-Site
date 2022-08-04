from rest_framework import viewsets

from ..models import Subject
from ..serializers import SubjectSerializer


class SubjectModelViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
