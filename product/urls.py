from django.urls import path
from . import views

urlpatterns = [
    path("", views.shop, name="shop"),
    path("brand/<str:brand>", views.shopByBrand, name="shopByBrand"),
    path("category/<str:category>", views.shopByCategory, name="shopByCategory"),
    path("gender/<str:gender>", views.shopByGender, name="shopByGender"),
    path("<int:id_product>", views.productDetail, name="productDetail"),
]
