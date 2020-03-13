from django import forms
from .models import Drama


class DateInput(forms.DateInput):
    input_type = "date"


class CreateDrama(forms.ModelForm):
    class Meta:
        model = Drama
        labels = {
            "mdlurl": "MDL URL",
            "epcount": "Episodes",
            "eplength": "Duration (Minutes)",
            "watchdate": "Watch Date",
        }
        fields = [
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
        widgets = {"watchdate": DateInput()}
