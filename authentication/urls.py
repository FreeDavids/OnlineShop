from django.urls import path
from .views import VRegister, log_out, log_in


urlpatterns = [
    path("", VRegister.as_view(), name="Authentication"),
    path("log_out", log_out, name="log_out"),
    path("log_in", log_in, name="log_in"),
]