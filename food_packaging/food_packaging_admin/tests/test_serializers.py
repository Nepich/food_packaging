from django.test import TestCase

from food_packaging_admin.serializers import LandingModelAdminSerializer
from food_packaging_admin.models import LandingModel


class LandingPageSerializerTestCase(TestCase):
    def test_ok(self):
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
            products_description="",
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
        data = LandingModelAdminSerializer(landing_page).data
        expected_data = {
            'products': [],
            'images': [],
            'employees': [],
            "top_utp": "Купите у нас",
            "top_descriptor": "Лучшие",
            "top_fb_url": "https://twitter.com/",
            "top_tw_url": "https://twitter.com/",
            "top_insta_url": "https://twitter.com/",
            "top_picture": None,
            "about_us_header": "ку",
            "about_us_text1": "ку",
            "about_us_text2": "ку",
            "about_us_picture1": None,
            "about_us_picture2": None,
            "about_us_value": "ку",
            "about_us_capacity": "ку",
            "about_us_employee": 3,
            "products_header": "ку",
            "products_description": "",
            "benefits_header": "ку",
            "benefits_first": "ку",
            "benefits_second": "ку",
            "benefits_third": "ку",
            "benefits_fourth": "ку",
            "benefits_fifth": "ку",
            "benefits_sixth": "ку",
            "benefits_seventh": "ку",
            "gallery_header": "ку",
            "team_header": "ку",
            "footer_address": "ку",
            "footer_email": "ку",
            "fax_footer": "ку"
        }
        self.assertEqual(expected_data, data)
