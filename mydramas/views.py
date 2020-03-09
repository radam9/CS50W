from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum

from .models import Drama, Network

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DramaSerializer, NetworkSerializer


def dashboard(request):
    data = dict()
    data["dramas"] = Drama.objects.all().count()
    data["favorites"] = Drama.objects.filter(favorite=True).count()
    episodes = Drama.objects.values_list("epcount", flat=True)
    data["episodes"] = sum(episodes)
    length = Drama.objects.values_list("eplength", flat=True)
    duration = float()
    for a, b in zip(episodes, length):
        duration += a * b / (60 * 24)
    data["duration"] = round(duration, 2)
    return render(request, "mydramas/dashboard.html", context={"data": data})


@api_view()
def favorite(request):
    data = dict()
    data["favpie"] = [
        {
            "category": "Favorites",
            "dramas": Drama.objects.filter(favorite=True).count(),
        },
        {"category": "Non-Favorites", "dramas": Drama.objects.all().count(),},
    ]
    years = list(
        Drama.objects.values_list("year", flat=True).distinct().order_by("year")
    )
    data["favarea"] = []
    for y in years:
        favorites = Drama.objects.filter(favorite=True, year=y).count()
        dramas = Drama.objects.filter(year=y).count()
        data["favarea"].append(
            {
                "Year": str(y),
                "Favorites": favorites,
                "Dramas": dramas,
                "Percent": round((favorites / dramas) * 100, 2),
            }
        )
    return Response(data)


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
