from django.contrib import admin
from .models import Menu, Order, Topping, Category

admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Topping)
admin.site.register(Category)
