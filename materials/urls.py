from django.urls import path
from rest_framework.routers import SimpleRouter
from materials.apps import MaterialsConfig

from materials.views import СourseViewSet, LessonCreateApiView, LessonUpdateApiView, LessonDestroyApiView, LessonListApiView, LessonRetriveApiView

app_name = MaterialsConfig.name
router = SimpleRouter()
router.register("", СourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lessons_list"),
    path("lessons/<int:pk>", LessonRetriveApiView.as_view(), name="lessons_retrive"),
    path("lessons/create/", LessonCreateApiView.as_view(), name="lessons_create"),
    path("lessons/<int:pk>/delete/", LessonDestroyApiView.as_view(), name="lessons_delete"),
    path("lessons/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lessons_update")
]

urlpatterns += router.urls