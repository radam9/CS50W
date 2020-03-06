from django.shortcuts import render
from django.http import HttpResponse


def dashboard(request):
    return render(request, "mydramas/dashboard.html")


def dramalist(request):
    return render(request, "mydramas/dramalist.html")


def home(request):
    return HttpResponse("<h1>Welcome to Home!</h1>")
