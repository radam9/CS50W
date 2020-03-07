from django.urls import path, include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("drama", views.DramaView)
router.register("network", views.NetworkView)

urlpatterns = [
    path("", views.home, name="home"),
    path("api/", include(router.urls)),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dramalist/", views.dramalist, name="dramalist"),
]
