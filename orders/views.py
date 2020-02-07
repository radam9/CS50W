from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "orders/base.html")


@login_required
def orders(request):
    return render(request, "orders/orders.html")
