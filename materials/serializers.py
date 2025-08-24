from django.core.serializers import serialize
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):

    count_lessons = SerializerMethodField()
    def get_count_lessons(self, course):
        return Lesson.objects.filter(course=course).count()


    class Meta:
        model = Course
        fields = ("name", "description", "count_lessons")


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"