from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    item = models.CharField(max_length=20)

    def __str__(self):
        return self.item

    class Meta:
        verbose_name_plural = "Categories"


class Menu(models.Model):
    t = [
        ("0", 0),
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
    ]
    item = models.CharField(max_length=30)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="menu_category"
    )
    tops = models.IntegerField(choices=t, default=0)
    sprice = models.DecimalField(max_digits=4, decimal_places=2)
    lprice = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.item} - {self.category} - S size ${self.sprice} - L size ${self.lprice}"


class Topping(models.Model):
    CATS = [("Pizza", "Pizza"), ("Sub", "Sub"), ("Steak+Cheese", "Steak+Cheese")]
    item = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATS)

    def __str__(self):
        return self.item


class Order(models.Model):
    STATUS = [
        ("Order Received", "Order Received"),
        ("Processing", "Processing"),
        ("On Route", "On Route"),
        ("Delivered", "Delivered"),
        ("None", ""),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_order")
    total = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS, default="None")

    def __str__(self):
        return f"User {self.user} - Total ${self.total} - Status {self.status}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_cart")


class OrderItem(models.Model):
    s = [("s", "Small"), ("l", "Large")]
    item = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    size = models.CharField(max_length=1, choices=s, blank=False, default="Large")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    toppings = models.ManyToManyField(Topping)
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, null=True, related_name="order_id"
    )
    cart = models.ForeignKey(
        Cart, on_delete=models.SET_NULL, null=True, related_name="cart_id"
    )

