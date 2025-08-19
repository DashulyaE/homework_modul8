from rest_framework.routers import SimpleRouter
from materials.apps import MaterialsConfig

from materials.views import СourseViewSet

app_name = MaterialsConfig.name
router = SimpleRouter()
router.register("", СourseViewSet)

urlpatterns = []

urlpatterns += router.urls