from .views import CarViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"cars", CarViewSet, basename="car")
urlpatterns = router.urls
