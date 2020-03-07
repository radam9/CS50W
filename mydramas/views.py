from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Drama, Network
from .serializers import DramaSerializer, NetworkSerializer


def dashboard(request):
    return render(request, "mydramas/dashboard.html")


def dramalist(request):
    dramas = Drama.objects.all().order_by("title")
    return render(request, "mydramas/dramalist.html", context={"dramas": dramas})


def home(request):
    return HttpResponse("<h1>Welcome to Home!</h1>")


class DramaView(viewsets.ModelViewSet):
    queryset = Drama.objects.all()
    serializer_class = DramaSerializer


class NetworkView(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
