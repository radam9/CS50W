from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .models import Drama, Network
from .forms import CreateDrama

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DramaSerializer, NetworkSerializer

from myscripts.MDL import getdramainfoview


@login_required
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
    # initializing JSON reponse data dictionary
    data = dict()
    # data for favorites piechart
    data["favpie"] = [
        {
            "category": "Favorites",
            "dramas": Drama.objects.filter(favorite=True).count(),
        },
        {
            "category": "Non-Favorites",
            "dramas": Drama.objects.filter(favorite=False).count(),
        },
    ]
    years = list(
        Drama.objects.values_list("year", flat=True).distinct().order_by("year")
    )
    # data for favorites areachart
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
    networks = Network.objects.values_list("title", flat=True)
    # data for network pichart1
    data["netpie1"] = []
    for n in networks:
        data["netpie1"].append(
            {"Network": n, "Dramas": Drama.objects.filter(network__title=n).count()}
        )
    # data for network linechart 1
    data["netline1"] = dict()
    data["netline1"]["data"] = []
    data["netline1"]["networks"] = networks
    for y in years:
        d = {"Year": str(y)}
        t = Drama.objects.filter(year=y).count()
        for n in networks:
            d[n] = Drama.objects.filter(network__title=n, year=y).count()
            if d[n] == 0:
                d[n + " " + "percent"] = 0
            else:
                d[n + " " + "percent"] = round((d[n] / t) * 100, 2)
        data["netline1"]["data"].append(d)
    # data for network pichart 2
    data["netpie2"] = []
    for n in networks:
        data["netpie2"].append(
            {
                "Network": n,
                "Dramas": Drama.objects.filter(network__title=n, favorite=True).count(),
            }
        )
    # data for network linechart 2
    data["netline2"] = dict()
    data["netline2"]["data"] = []
    data["netline2"]["networks"] = networks
    for y in years:
        d = {"Year": str(y)}
        t = Drama.objects.filter(year=y, favorite=True).count()
        for n in networks:
            d[n] = Drama.objects.filter(network__title=n, year=y, favorite=True).count()
            if d[n] == 0:
                d[n + " " + "percent"] = 0
            else:
                d[n + " " + "percent"] = round((d[n] / t) * 100, 2)
        data["netline2"]["data"].append(d)
    # data for rating piechart 1
    ratings = list(
        Drama.objects.values_list("rating", flat=True).distinct().order_by("-rating")
    )
    data["ratingpie1"] = []
    for r in ratings:
        data["ratingpie1"].append(
            {"rating": str(r), "Dramas": Drama.objects.filter(rating=r).count()}
        )
    # data for rating historgram 1
    data["ratinghisto1"] = dict()
    data["ratinghisto1"]["data"] = []
    data["ratinghisto1"]["ratings"] = ratings
    for y in years:
        d = {"Year": str(y)}
        t = Drama.objects.filter(year=y).count()
        for r in ratings:
            r = str(r)
            d[r] = Drama.objects.filter(rating=r, year=y).count()
            if d[r] == 0:
                d[r + " " + "percent"] = 0
            else:
                d[r + " " + "percent"] = round((d[r] / t) * 100, 2)
        data["ratinghisto1"]["data"].append(d)
    return Response(data)


class DramaListView(ListView):
    model = Drama
    template_name = "mydramas/dramalist.html"
    ordering = ["title"]


class DramaCreateView(CreateView):
    # model = Drama
    # fields = [
    #     "title",
    #     "year",
    #     "network",
    #     "rating",
    #     "mdlurl",
    #     "favorite",
    #     "epcount",
    #     "eplength",
    #     "watchdate",
    # ]
    form_class = CreateDrama
    template_name = "mydramas/newdrama.html"
    success_url = "dramalist/"


@api_view()
def fetchdrama(request):
    url = request.headers["url"]
    t = getdramainfoview(url)
    data = {
        "title": t[0],
        "epcount": t[1],
        "year": t[2],
        "network": t[3],
        "eplength": t[4],
        "image": t[5],
    }
    return Response(data)


@login_required
def newdrama(request):
    if request.method == "POST":
        form = CreateDrama()

    if request.method == "GET":
        form = CreateDrama()
        return render(request, "mydramas/newdrama.html", context={"form": form})


class DramaView(viewsets.ModelViewSet):
    queryset = Drama.objects.all()
    serializer_class = DramaSerializer


class NetworkView(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
