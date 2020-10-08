from django import forms

from .models import City, Quote, ZIP


class QuoteForm(forms.ModelForm):

    city = forms.CharField(max_length=250)
    zip_code = forms.CharField(max_length=5, label="ZIP Code")

    field_order = [
        "first_name",
        "last_name",
        "phone_number",
        "email",
        "street_1",
        "street_2",
        "city",
        "zip_code",
        "no_contact",
        "special_offer",
    ]

    class Meta:
        model = Quote
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "street_1",
            "street_2",
            "no_contact",
            "special_offer",
        ]
        widgets = {"special_offer": forms.HiddenInput()}

    def save(self, commit=True):
        self.instance.city = City.objects.get_or_create(
            name=self.cleaned_data.get("city")
        )[0]
        self.instance.zip_code = ZIP.objects.get_or_create(
            code=self.cleaned_data.get("zip_code")
        )[0]
        return super().save(commit)
