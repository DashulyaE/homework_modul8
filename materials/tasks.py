from celery import shared_task

from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


@shared_task
def send_update_curse(user_email, course_name):
    subject = f'Обновление курса: {course_name}'
    message = f'Здравствуйте! В курсе "{course_name}" произошли обновления. Подробнее на сайте.'
    send_mail(subject, message, EMAIL_HOST_USER, [user_email])