from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'product/<int:pk>/',
        views.product_detail,
        name='product_detail'
    ),

    path(
        'cart/',
        views.cart,
        name='cart'
    ),

    path(
        'add-to-cart/<int:pk>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),

    path(
        'increase/<int:pk>/',
        views.increase_quantity,
        name='increase'
    ),

    path(
        'decrease/<int:pk>/',
        views.decrease_quantity,
        name='decrease'
    ),

    path(
        'remove/<int:pk>/',
        views.remove_cart,
        name='remove_cart'
    ),

]