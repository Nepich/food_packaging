from django.urls import path
from .views import LandingPageView, LandingPageFormView

urlpatterns = [
    path('', LandingPageView.as_view(), name='get_request'),
    path('create/', LandingPageFormView.as_view()),
]