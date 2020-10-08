from django.core.mail import mail_managers
from django.db import models
from django.template.loader import render_to_string

from model_utils.models import TimeStampedModel


class City(models.Model):

    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Quote(TimeStampedModel):
    first_name = models.CharField(max_length=120, verbose_name="First Name")
    last_name = models.CharField(max_length=120, verbose_name="Last Name")
    phone_number = models.CharField(
        max_length=14,
        help_text="eg. (386) 123-4567",
        verbose_name="Phone Number"
    )
    email = models.EmailField()
    street_1 = models.CharField(max_length=250, verbose_name="Address Line")
    street_2 = models.CharField(
        max_length=250, null=True, blank=True, verbose_name="Address Line 2"
    )
    city = models.ForeignKey("City", on_delete=models.PROTECT)
    zip_code = models.ForeignKey(
        "ZIP", on_delete=models.PROTECT, verbose_name="ZIP Code"
    )
    no_contact = models.BooleanField(
        default=False,
        verbose_name="No Contact Quote",
        help_text=(
            "If selected, we will notify you by text message once we "
            "have arrived at your property. We will then perform a walk "
            "around of your property to be able to provide a accurate quote. "
            "Once complete, we will follow up with a quote by email."
        )
    )
    sent = models.BooleanField(default=False)
    reviewed = models.BooleanField(default=False)
    special_offer = models.ForeignKey(
        "special_offer.SpecialOffer",
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Quote for {self.full_name()}"

    @classmethod
    def send_quotes(cls):
        quotes = cls.objects.filter(sent=False)
        if quotes:
            for quote in quotes:
                quote.send_quote()
                quote.sent = True
                quote.save()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def send_quote(self):
        context = {"quote": self, "subject": "New Quote Request",}
        body = render_to_string("quote/email/quote.txt", context)
        html = render_to_string("quote/email/quote.html", context)
        mail_managers(
            subject=context["subject"], message=body, html_message=html
        )


class ZIP(models.Model):

    code = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.code
