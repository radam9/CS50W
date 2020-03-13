from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from orders.models import Cart
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Your account has been created, you can now login"
            )
            # create a databse Cart for the new user.
            username = request.POST["username"]
            userid = User.objects.get(username=username).id
            cart = Cart(user_id=userid)
            cart.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})

