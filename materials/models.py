from django.db import models


class Сourse(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название курса")
    preview = models.ImageField(
        upload_to="materials/course/",
        verbose_name="Превью",
        blank=True,
        null=True,
        help_text="Превью курса",
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание курса")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    course = models.ForeignKey(Сourse, on_delete=models.SET_NULL, null=True, related_name='lessons', verbose_name="Курс")
    name = models.CharField(max_length=100, verbose_name="Название урока")
    preview = models.ImageField(
        upload_to="materials/lesson/",
        verbose_name="Превью",
        blank=True,
        null=True,
        help_text="Превью урока",
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание урока")
    video_link = models.URLField()
    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"