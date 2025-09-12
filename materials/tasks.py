from datetime import timedelta

from celery import shared_task

from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from users.models import User


@shared_task
def send_update_curse(user_email, course_name):
    """Отправка письма письма пользователю об изменениях в курсе"""

    subject = f'Обновление курса: {course_name}'
    message = f'Здравствуйте! В курсе "{course_name}" произошли обновления. Подробнее на сайте.'
    send_mail(subject, message, EMAIL_HOST_USER, [user_email])


@shared_task
def check_last_login():
    """Проверка последнего входа пользователей и отключение неактивных пользователей"""

    users = User.objects.filter(last_login__isnull=False)
    today = timezone.now()
    for user in users:
        if today - user.last_login > timedelta(days=30):
            user.is_active = False
            user.save()
            print(f"Пользователь {user.email} отключен")
        else:
            print(f"Пользователь {user.email} активен")