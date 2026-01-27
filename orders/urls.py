from .views import CreateMyOrderProductView, MyOrderView
from django.urls import path



urlpatterns = [
    path("mi-orden", MyOrderView.as_view(), name="my_order"),
    path("agregar-producto", CreateMyOrderProductView.as_view(), name="add_product_to_order"),
]