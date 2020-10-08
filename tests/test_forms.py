from django.test import TestCase

from model_bakery import baker

from ..forms import QuoteForm
from ..models import City, ZIP


class QuoteFormTest(TestCase):

    def test_save_new(self):
        # setup
        form = QuoteForm(data={
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "(386) 999-9999",
            "email": "jdoes@test.com",
            "street_1": "123 Easy St.",
            "street_2": "Unit 123",
            "city": "Daytona Beach",
            "zip_code": "32119",
        })
        form.is_valid()
        quote = form.save()

        # asserts
        self.assertEqual(quote.city.name, "Daytona Beach")
        self.assertEqual(quote.zip_code.code, "32119")
        self.assertEqual(City.objects.count(), 1)
        self.assertEqual(ZIP.objects.count(), 1)

    def test_save_exists(self):
        # setup
        baker.make(City, name="Daytona Beach")
        baker.make(ZIP, code="32119")
        form = QuoteForm(data={
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "(386) 999-9999",
            "email": "jdoes@test.com",
            "street_1": "123 Easy St.",
            "street_2": "Unit 123",
            "city": "Daytona Beach",
            "zip_code": "32119",
        })
        form.is_valid()
        quote = form.save()

        # asserts
        self.assertEqual(quote.city.name, "Daytona Beach")
        self.assertEqual(quote.zip_code.code, "32119")
        self.assertEqual(City.objects.count(), 1)
        self.assertEqual(ZIP.objects.count(), 1)
