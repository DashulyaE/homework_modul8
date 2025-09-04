from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from materials.models import Course, Lesson, CourseSubscription
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

    def test_course_create(self):
        url = reverse("materials:course-list")
        data = {
            "name": "Курс 2",
            "description": "Описание курса 2"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Course.objects.all().count(), 2
        )

    def test_course_update(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        data = {
            "name": "Курс 1 изм "
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
           data.get("name"), "Курс 1 изм"
        )

    def test_course_delete(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
           Course.objects.all().count(), 0
        )

    def test_course_list(self):
        url = reverse("materials:course-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.course.pk,
                    "is_subscribed": False,
                    "name": self.course.name,
                    "preview": None,
                    "description": self.course.description,
                    "owner": self.user.pk
                }
            ]
        }
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@test.ru")
        self.course = Course.objects.create(name="Курс 1", description="Описание курса 1", owner=self.user)
        self.lesson = Lesson.objects.create(course=self.course, name="Урок 1", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrive(self):
        url = reverse("materials:lessons-retrive", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
           data.get("name"), self.lesson.name
        )

    def test_lesson_create(self):
        url = reverse("materials:lessons-create")
        data = {
            "name": "Урок 2"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_update(self):
        url = reverse("materials:lessons-update", args=(self.lesson.pk,))
        data = {
            "name": "Урок 1 изм "
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
           data.get("name"), "Урок 1 изм"
        )

    def test_lesson_delete(self):
        url = reverse("materials:lessons-delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse("materials:lessons-list")
        response = self.client.get(url)
        data = response.json()
        result = {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.lesson.pk,
                        "name": self.lesson.name,
                        "preview": None,
                        "description": None,
                        "video_link": None,
                        "course": self.course.pk,
                        "owner": self.user.pk
                    }
                ]
        }
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )


class SubscriptionViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email="admin@test.ru")
        self.course = Course.objects.create(name="Курс 1", description="Описание курса 1", owner=self.user)
        self.lesson = Lesson.objects.create(course=self.course, name="Урок 1", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscribe_to_course(self):
        url = reverse("materials:course-subscribe", args=(self.course.pk,))
        response = self.client.post(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'подписка добавлена')
        self.assertTrue(CourseSubscription.objects.filter(user=self.user, course=self.course).exists())

    def test_unsubscribe_from_course(self):
        # сначала подписываемся
        CourseSubscription.objects.create(user=self.user, course=self.course)
        url = reverse("materials:course-subscribe", args=(self.course.pk,))
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'подписка удалена')
        self.assertFalse(CourseSubscription.objects.filter(user=self.user, course=self.course).exists())

    def test_delete_subscription_when_exists(self):
        CourseSubscription.objects.create(user=self.user, course=self.course)
        url = reverse("materials:course-subscribe", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'подписка удалена')
        self.assertFalse(CourseSubscription.objects.filter(user=self.user, course=self.course).exists())

    def test_delete_subscription_when_not_exists(self):
        url = reverse("materials:course-subscribe", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'подписка не найдена')

