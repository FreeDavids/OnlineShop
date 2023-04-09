from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("add/<int:product_id>/", views.add_product, name="add"),
    path("remove/<int:product_id>/", views.remove_product, name="remove"),
    path("subtract/<int:product_id>/", views.subtract_product, name="subtract"),
    path("clean", views.clean_all_cart, name="clean"),
]