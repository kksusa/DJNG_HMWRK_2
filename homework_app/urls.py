from django.urls import path
from .views import get_orders_by_user_id
from .views import get_products_by_user_id
from .views import edit_product
from .views import get_product_by_id


urlpatterns = [
    path('get_orders/<int:user_id>/', get_orders_by_user_id),
    path('get_products/<int:user_id>/<str:period>/', get_products_by_user_id),
    path('edit_product/', edit_product),
    path('get_product/<int:product_id>/', get_product_by_id),
]