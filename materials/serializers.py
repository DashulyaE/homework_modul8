from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson
from materials.validators import validate_link


class CourseSerializer(ModelSerializer):
    """Сериализатор для модели Курс"""

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    """Сериализатор для модели Урок"""

    class Meta:
        model = Lesson
        fields = "__all__"

    def validate(self, data):
        video_link = data.get('video_link')
        if video_link:
            validate_link(video_link)
        return data

class CourseDetailSerializer(ModelSerializer):
    """Сериализатор для одного объекта модели Курс"""

    count_lessons = SerializerMethodField()
    lessons = LessonSerializer(many=True)

    def get_count_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ("name", "description", "count_lessons", "lessons")
