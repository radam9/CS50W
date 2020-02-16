from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from orders.models import Menu, Topping, OrderItem, Cart
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
    t = loader.get_template("orders/modal.html")
    if request.method == "POST":
        i = int(request.POST["itemid"])
        item = Menu.objects.get(id=i)
        cart = Cart.objects.get(user_id=request.user.id)
        r = {
            "item": item.item,
            "itemid": i,
            "category": item.category.item,
            "size": request.POST["size"],
            "price": float(request.POST["price"]),
            "quantity": int(request.POST["quantity"]),
            "cart": cart,
            "toppings": request.POST.getlist("toppings[]"),
        }
        form = CreateOrderItem(r, x=i)
        if form.is_valid():
            print("isvalid")
            r.pop("itemid")
            toppingspop = r.pop("toppings")
            orditem = OrderItem(**r)
            orditem.save()
            if len(toppingspop) > 0:
                orditem.toppings.set(toppingspop)
                orditem.save()

            return HttpResponse("it was a success!", status=200)
        else:
            return HttpResponse(t.render({"form": form}, request), status=422)

    elif request.method == "GET":
        i = int(request.GET["item"])
        item = Menu.objects.get(id=i)
        form = CreateOrderItem(x=i, initial={"size": "l"})
        return HttpResponse(t.render({"item": item, "form": form}, request))


def myorders(request):
    pass


def cart(request):
    return render(request, "orders/cart.html")
