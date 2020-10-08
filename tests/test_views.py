from django.test import TestCase
from django.urls import reverse

from ..views import QuoteCreate


class QuoteCreateTest(TestCase):

    def test_get_success_url(self):
        # setup
        response = self.client.post(
            reverse("quote:quote_create"), {
                "first_name": "John",
                "last_name": "Doe",
                "phone_number": "3869999999",
                "email": "test@test.com",
                "street_1": "123 easy st",
                "city": "Daytona Beach",
                "zip_code": "32114"
            }
        )

        # asserts
        self.assertEqual(
            response.url, "/quotes/success/#success_message"
        )
