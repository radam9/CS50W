from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    item = models.CharField(max_length=20)

    def __str__(self):
        return self.item

    class Meta:
        verbose_name_plural = "Categories"


class Menu(models.Model):
    item = models.CharField(max_length=30)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="menu_category"
    )
    sprice = models.DecimalField(max_digits=4, decimal_places=2)
    lprice = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.item} - {self.category} - S size ${self.sprice} - L size ${self.lprice}"


class Topping(models.Model):
    item = models.CharField(max_length=20)

    def __str__(self):
        return self.item


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET("User Deleted"), related_name="user_order"
    )
    contents = models.TextField()
    total = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=15)

    def __str__(self):
        return f"Order no.25 by customer no.{self.user} for ${self.total} is currently {self.status}"

