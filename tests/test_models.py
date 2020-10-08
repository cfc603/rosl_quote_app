from unittest.mock import patch

from django.template.loader import render_to_string
from django.test import TestCase

from model_bakery import baker

from ..models import Quote


class CityTest(TestCase):

    def test_str(self):
        # setup
        city = baker.make("quote.City", name="Daytona Beach")

        # asserts
        self.assertEqual(city.__str__(), "Daytona Beach")


class QuoteTest(TestCase):

    def test_str(self):
        # setup
        quote = baker.make("quote.Quote", first_name="John", last_name="Doe")

        # asserts
        self.assertEqual(quote.__str__(), "Quote for John Doe")

    def test_full_name(self):
        # setup
        quote = baker.make("quote.Quote", first_name="John", last_name="Doe")

        # asserts
        self.assertEqual(quote.full_name(), "John Doe")

    @patch("quote.models.Quote.send_quote")
    def test_send_quotes_if_exists(self, mock_send):
        # setup
        baker.make("quote.Quote", sent=False)
        Quote.send_quotes()

        # asserts
        self.assertFalse(
            Quote.objects.filter(sent=False).exists()
        )
        mock_send.assert_called_once()

    @patch("quote.models.Quote.send_quote")
    def test_send_quotes_if_not_exists(self, mock_send):
        # setup
        baker.make("quote.Quote", sent=True)
        Quote.send_quotes()

        # asserts
        self.assertFalse(
            Quote.objects.filter(sent=False).exists()
        )
        mock_send.assert_not_called()

    @patch("quote.models.mail_managers")
    def test_send_quote(self, mock_mail_managers):
        # setup
        obj = baker.make("quote.Quote")
        obj.send_quote()
        context = {"quote": obj, "subject": "New Quote Request",}
        body = render_to_string("quote/email/quote.txt", context)
        html = render_to_string("quote/email/quote.html", context)

        # asse rts
        mock_mail_managers.assert_called_once_with(
            subject="New Quote Request", message=body, html_message=html
        )


class ZIPTest(TestCase):

    def test_str(self):
        # setup
        zip_ = baker.make("quote.ZIP", code="32114")

        # asserts
        self.assertEqual(zip_.__str__(), "32114")
