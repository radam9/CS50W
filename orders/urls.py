from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("menu/", views.menu, name="menu"),
    path("cart/", views.cart, name="cart"),
    path("myorders/", views.myorders, name="myorders"),
    path("modal/", views.modal, name="modal"),
]
