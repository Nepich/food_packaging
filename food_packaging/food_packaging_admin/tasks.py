from django.core.mail import send_mail
from food_packaging.celery import app


@app.task
def send_email(recipient, name, phone, message):
    send_mail('Новая заявка',
              f'У вас новая заявка от пользователя - {name}\n'
              f'Номер телефона - {phone}\n'
              f'Сообщение: {message}',
              'nepich@gmail.com',
              [recipient],
              fail_silently=False)
