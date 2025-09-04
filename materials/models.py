from django.db import models

from config import settings


class Course(models.Model):
    """Модель Курс"""

    name = models.CharField(max_length=100, verbose_name="Название курса")
    preview = models.ImageField(
        upload_to="materials/course/",
        verbose_name="Превью",
        blank=True,
        null=True,
        help_text="Превью курса",
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание курса")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец курса",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    """Модель Урок"""

    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        related_name="lessons",
        verbose_name="Курс",
    )
    name = models.CharField(max_length=100, verbose_name="Название урока")
    preview = models.ImageField(
        upload_to="materials/lesson/",
        verbose_name="Превью",
        blank=True,
        null=True,
        help_text="Превью урока",
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание урока")
    video_link = models.URLField(
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец урока",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class CourseSubscription(models.Model):
    """Модель Подсписка на курс """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="course_subscriptions",
    )
    course = models.ForeignKey(
        "Course", on_delete=models.CASCADE, related_name="subscriptions"
    )
    subscribed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "course")
        verbose_name = "Подписка на курс"
        verbose_name_plural = "Подписки на курсы"
