from django.urls import path, include
from services import views

urlpatterns = [
    path('', views.services, name="Services"),
]
