from django.core.mail import send_mail

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

from .models import LandingModel, ManagersModel, FormBlockAdminModel
from .serializers import LandingModelAdminSerializer, FormBlockSerializer


class LandingPageFormView(CreateAPIView):
    """View to send a form"""
    serializer_class = FormBlockSerializer
    queryset = FormBlockAdminModel.objects.all()

    def perform_create(self, serializer):
        mail_to = ManagersModel.objects.all().values()
        queryset = self.get_queryset().values()[0]
        for recipient in mail_to:
            send_mail('Новая заявка',
                      f'У вас новая заявка от пользователя - {queryset["form_customer_name"]}\n'
                      f'Номер телефона - {queryset["form_customer_phone"]}\n'
                      f'Сообщение: {queryset["form_customer_message"]}',
                      'nepich@gmail.com',
                      [recipient['managers_email']],
                      fail_silently=False)


class LandingPageView(APIView):
    """View to get landing context"""
    def get(self, request, *args, **kwargs):
        queryset = LandingModel.objects.latest('id')
        serializer = LandingModelAdminSerializer(queryset)
        return Response(serializer.data)





