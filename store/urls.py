from django.urls import path
from .views import product_list, create_product, update_product, delete_product

urlpatterns = [
    path("", product_list, name="product_list"),
    path("create/", create_product, name="create_product"),
    path("update/<str:sku>/", update_product, name="update_product"),
    path("delete/<str:sku>/", delete_product, name="delete_product"),
]