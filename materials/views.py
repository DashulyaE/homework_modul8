from rest_framework.viewsets import ModelViewSet

from materials.models import Course
from materials.serializers import CourseSerializer


class СourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer