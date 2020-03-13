from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from orders.models import Menu, Topping, OrderItem, Cart, Order
from orders.forms import CreateOrderItem


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
    t = loader.get_template("orders/modalmenu.html")
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
        form = CreateOrderItem(x=i, initial={"size": "Large"})
        return HttpResponse(t.render({"item": item, "form": form}, request))


def myorders(request):
    if request.user.is_staff:
        orders = Order.objects.all().order_by("-date")
    else:
        orders = Order.objects.filter(user_id=request.user.id).order_by("-date")
    return render(request, "orders/myorders.html", context={"orders": orders})


def cart(request):
    if request.method == "POST":
        if "itemid" in request.POST:
            itemid = request.POST["itemid"]
            orderitem = OrderItem.objects.get(id=itemid)
            price = str(round(float(orderitem.price), 2))
            orderitem.delete()
            return JsonResponse({"price": price})
        else:
            cid = Cart.objects.get(user_id=request.user.id).id
            cart = OrderItem.objects.filter(cart=cid)
            if len(cart) == 0:
                pass
            else:
                order = Order(user=request.user)
                order.save()
                cart = OrderItem.objects.filter(cart=cid)
                tot = 0
                for c in cart:
                    c.order = order
                    c.cart = None
                    tot += float(c.price)
                    c.save()
                total = round(tot, 2)
                order.total = total
                order.save()
                return redirect("myorders")

    if request.method == "GET":
        cid = Cart.objects.get(user_id=request.user.id).id
        cart = OrderItem.objects.filter(cart=cid)
        orders, total = templatecart(cart)
        return render(
            request, "orders/cart.html", context={"orders": orders, "total": total}
        )


def modalcart(request):
    t = loader.get_template("orders/modalcart.html")
    cid = Cart.objects.get(user_id=request.user.id).id
    cart = OrderItem.objects.filter(cart=cid)
    orders, total = templatecart(cart)
    return HttpResponse(t.render({"orders": orders, "total": total}, request))


# function to return list of order items and total price
def templatecart(cart):
    orders = []
    tot = 0
    for c in cart:
        t = (" - ").join(list(c.toppings.values_list("item", flat=True)))
        tot += float(c.price)
        orders.append(
            {
                "id": int(c.id),
                "item": c.item,
                "category": c.category,
                "price": round(float(c.price), 2),
                "size": c.size,
                "toppings": t,
            }
        )
    total = round(tot, 2)
    return orders, total
