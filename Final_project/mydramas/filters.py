from .models import Drama
import django_filters


class DramaFilter(django_filters.FilterSet):
    CHOICES = (
        ("title", "Title - Ascending"),
        ("-title", "Title - Descending"),
        ("year", "Year - Ascending"),
        ("-year", "Year - Descending"),
        ("network", "Network - Ascending"),
        ("-network", "Network - Descending"),
        ("rating", "Rating - Ascending"),
        ("-rating", "Rating - Descending"),
        ("favorite", "Favorite - Ascending"),
        ("-favorite", "Favorite - Descending"),
    )
    ordering = django_filters.ChoiceFilter(
        label="Sort by", choices=CHOICES, method="filter_order"
    )

    class Meta:
        model = Drama
        fields = {
            "title": ["icontains"],
            "year": ["exact"],
            "network": ["exact"],
            "rating": ["exact"],
            "favorite": ["exact"],
        }

    def filter_order(self, queryset, name, value):
        return queryset.order_by(value)
