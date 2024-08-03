from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(prefix='jobs', viewset=views.JobViewSet, basename='job')
router.register(prefix='companies', viewset=views.CompanyViewSet, basename='company')

urlpatterns = router.urls