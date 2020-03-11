from django import forms
from .models import Drama


class CreateDrama(forms.ModelForm):
    watchdate = forms.DateField(
        input_formats=["%d/%m/%Y"],
        widget=forms.DateInput(
            attrs={
                "class": "form-control datetimepicker-input",
                "data-target": "#datetimepicker1",
            }
        ),
    )

    class Meta:
        model = Drama
        labels = {
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
