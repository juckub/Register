from rest_framework import routers
from .views import HumanViewSet


router = routers.DefaultRouter()


router.register('human', HumanViewSet)

urlpatterns = router.urls
