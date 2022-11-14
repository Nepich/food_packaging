import logging

from django.core.mail import send_mail

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

from .models import LandingModel, ManagersModel, FormBlockAdminModel
from .serializers import LandingModelAdminSerializer, FormBlockSerializer
from .tasks import send_email

logger = logging.getLogger('main')


class LandingPageFormView(CreateAPIView):
    """View to send a form"""
    serializer_class = FormBlockSerializer
    queryset = FormBlockAdminModel.objects.all()

    def perform_create(self, serializer):
        try:
            mail_to = ManagersModel.objects.all().values()
            data = self.request.data
            name = data["form_customer_name"]
            phone = data["form_customer_phone"]
            message = data["form_customer_phone"]
            for recipient in mail_to:
                send_to = recipient['managers_email']
                send_email.delay(send_to, name, phone, message)
            serializer.save()
        except Exception as e:
            logger.warning(e)


class LandingPageView(APIView):
    """View to get landing context"""

    def get(self, request, *args, **kwargs):
        try:
            queryset = LandingModel.objects.latest('id')
            serializer = LandingModelAdminSerializer(queryset)
            return Response(serializer.data)
        except Exception as e:
            logger.warning(e)






