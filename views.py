from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import QuoteForm
from .models import Quote


class QuoteCreate(CreateView):

    form_class = QuoteForm
    model = Quote
    success_url = reverse_lazy("quote:quote_success")

    def get_success_url(self):
        return super().get_success_url() + "#success_message"


class QuoteSuccess(TemplateView):

    template_name = "quote/quote_success.html"
