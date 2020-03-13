from django.urls import path, include
from django.contrib.auth.decorators import login_required

from . import views
from .views import DramaListView, DramaCreateView, DramaDownloadView

from rest_framework import routers

router = routers.DefaultRouter()
router.register("drama", views.DramaView)
router.register("network", views.NetworkView)

urlpatterns = [
    path("api/", login_required(include(router.urls))),
    path("api/favorite/", views.favorite, name="favorite"),
    path("api/fetchdrama/", views.fetchdrama, name="fetchdrama"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dramalist/", login_required(DramaListView.as_view()), name="dramalist"),
    path(
        "dramalist/<str:file_type>/",
        login_required(DramaDownloadView.as_view()),
        name="download_file",
    ),
    path("newdrama/", login_required(DramaCreateView.as_view()), name="newdrama"),
]
