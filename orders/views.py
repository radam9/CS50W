from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from orders.models import Menu, Topping
from django.db.models import Q
from orders.forms import CreateOrderItem


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


def modal(request):
    i = int(request.GET["item"][5::])
    item = Menu.objects.filter(id=i)[0]
    form = CreateOrderItem()
    # changing the queryset contents (the toppings showin in the modal)
    if item.category.item == "Regular Pizza" or item.category.item == "Sicilian Pizza":
        form.fields["toppings"].queryset = Topping.objects.filter(category="Pizza")
    elif item.category.item == "Sub" and item.item == "Steak + Cheese":
        form.fields["toppings"].queryset = Topping.objects.filter(
            Q(category="Steak+Cheese") | Q(category="Sub")
        )
    else:
        form.fields["toppings"].queryset = Topping.objects.filter(category="Sub")

    t = loader.get_template("orders/modal.html")
    return HttpResponse(t.render({"item": item, "form": form}, request))


def myorders(request):
    pass


def cart(request):
    return render(request, "orders/cart.html")
