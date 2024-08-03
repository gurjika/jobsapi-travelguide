from rest_framework.viewsets import ModelViewSet
from jobs_api.models import Job
from jobs_api.serializers import JobSerializer
# Create your views here.


class JobViewSet(ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
