from rest_framework.viewsets import ModelViewSet
from jobs_api.models import Company, Job
from jobs_api.serializers import CompanySerializer, JobSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class JobViewSet(ModelViewSet):
    """
    A viewset for viewing and editing Job instances.
    
    - `serializer_class`: The serializer class used for this viewset.
    - `queryset`: The queryset used to retrieve Job instances. Uses select_related to optimize database access.
    - `permission_classes`: List of permission classes that determine access to this viewset.
    - `filter_backends`: List of filter backends used to filter the queryset.
    - `filterset_fields`: List of fields that can be used for filtering the queryset.
    """
    serializer_class = JobSerializer
    queryset = Job.objects.select_related('company__created_by').all()
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']

    
class CompanyViewSet(ModelViewSet):

    """
    A viewset for viewing and editing Company instances.
    
    - `serializer_class`: The serializer class used for this viewset.
    - `queryset`: The queryset used to retrieve Company instances. Uses select_related to optimize database access.
    - `permission_classes`: List of permission classes that determine access to this viewset.
    """
    serializer_class = CompanySerializer
    queryset = Company.objects.select_related('created_by').all()
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    

    def get_serializer_context(self):
        return { 'user': self.request.user }
