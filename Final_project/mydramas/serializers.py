from rest_framework import serializers
from .models import Drama, Network


class DramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drama
        fields = (
            "title",
            "year",
            "network",
            "rating",
            "mdlurl",
            "favorite",
            "epcount",
            "eplength",
            "watchdate",
        )


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ("title",)

