from django.urls import path

from quote import views

app_name = "quote"
urlpatterns = [
    path("create/", views.QuoteCreate.as_view(), name="quote_create"),
    path("success/", views.QuoteSuccess.as_view(), name="quote_success"),
]
