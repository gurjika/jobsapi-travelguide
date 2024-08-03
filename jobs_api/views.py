from rest_framework.viewsets import ModelViewSet
from jobs_api.models import Job
from jobs_api.serializers import JobSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly

# Create your views here.


class JobViewSet(ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


    def get_serializer_context(self):
        return {'user': self.request.user}