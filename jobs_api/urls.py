from rest_framework import routers
from . import views

router = routers.DefaultRouter()


router.register(prefix='jobs', viewset=views.JobViewSet, basename='job')

urlpatterns = router.urls