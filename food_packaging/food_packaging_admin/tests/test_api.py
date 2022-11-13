from django.urls import reverse, path, include
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from food_packaging_admin.models import LandingModel
from food_packaging_admin.serializers import LandingModelAdminSerializer


class LandingApiTestCase(APITestCase):

    def test_get(self):
        landing_page = LandingModel.objects.create(
            top_utp="Купите у нас",
            top_descriptor="Лучшие",
            top_fb_url="https://twitter.com/",
            top_tw_url="https://twitter.com/",
            top_insta_url="https://twitter.com/",
            top_picture="",
            about_us_header="ку",
            about_us_text1="ку",
            about_us_text2="ку",
            about_us_picture1="",
            about_us_picture2="",
            about_us_value="ку",
            about_us_capacity="ку",
            about_us_employee="3",
            products_header="ку",
            products_description="ку",
            benefits_header="ку",
            benefits_first="ку",
            benefits_second="ку",
            benefits_third="ку",
            benefits_fourth="ку",
            benefits_fifth="ку",
            benefits_sixth="ку",
            benefits_seventh="ку",
            gallery_header="ку",
            team_header="ку",
            footer_address="ку",
            footer_email="ку",
            fax_footer="ку",
        )
        url = reverse('get_request')
        response = self.client.get(url)
        serializer_data = LandingModelAdminSerializer(landing_page).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
