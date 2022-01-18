from celery import shared_task
from django.core.mail import send_mail

"""
Асинхронная задача для отправки почты участнику
"""
@shared_task
def match_created(match_name,match_email,mail_to):
    subject = f'You has been liked'
    message = f'Вы понравились {match_name}! Почта участника: {match_email}'
    mail_sent = send_mail(subject,
                          message,
                          'dating@gmail.com',
                          [mail_to])
    return mail_sent