from django.contrib import admin
from .models import Network, Drama


class NetworkAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_editable = ["title"]
    list_display_links = ["id"]


class DramaAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "year",
        "network",
        "rating",
        "mdlurl",
        "favorite",
        "epcount",
        "eplength",
        "watchdate",
    ]
    search_fields = [
        "title",
        "year",
        "network",
        "rating",
        "favorite",
        "epcount",
        "eplength",
        "watchdate",
    ]
    list_filter = ["year", "network", "rating", "favorite", "epcount"]
    list_display_links = ["id"]


admin.site.register(Network, NetworkAdmin)
admin.site.register(Drama, DramaAdmin)
