from django.urls import path
from . import views

urlpatterns = [
    path("", views.shop, name="shop"),
    path("<int:id_product>", views.productDetail, name="productDetail"),
]
