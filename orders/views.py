from django.shortcuts import render
from orders.models import Menu

# Create your views here.
def home(request):
    return render(request, "orders/home.html")


def menu(request):
    regular = Menu.objects.filter(category__item="Regular Pizza")
    sicilian = Menu.objects.filter(category__item="Sicilian Pizza")
    subs = Menu.objects.filter(category__item="Sub")
    subl = subs[::2]
    subr = subs[1::2]
    pasta = Menu.objects.filter(category__item="Pasta")
    salad = Menu.objects.filter(category__item="Salad")
    dinner = Menu.objects.filter(category__item="Dinner Platter")
    dinnerl = dinner[::2]
    dinnerr = dinner[1::2]
    menu = {
        "regular": regular,
        "sicilian": sicilian,
        "subl": subl,
        "subr": subr,
        "pasta": pasta,
        "salad": salad,
        "dinnerl": dinnerl,
        "dinnerr": dinnerr,
    }
    return render(request, "orders/menu.html", context=menu)

