from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@test.ru")
        self.course = Course.objects.create(name="Курс 1", description="Описание курса 1", owner=self.user)
        self.lesson = Lesson.objects.create(course=self.course, name="Урок 1", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_course_retrive(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
           data.get("name"), self.course.name
        )



