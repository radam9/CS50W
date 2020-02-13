from django import forms
from django.db.models import Q
from orders.models import OrderItem, Topping, Menu


class CreateOrderItem(forms.ModelForm):
    class Meta:
        model = OrderItem
        exclude = []
        fields = ["toppings", "size", "quantity"]
        widgets = {
            "toppings": forms.SelectMultiple(),
            "size": forms.RadioSelect(),
            "quantity": forms.NumberInput(
                attrs={"value": 1, "min": 1, "max": 25, "step": 1}
            ),
        }

    def __init__(self, *args, **kwargs):
        self.i = kwargs.pop("x")
        item = Menu.objects.filter(id=self.i)[0]

        super(CreateOrderItem, self).__init__(self, *args, **kwargs)

        if (
            item.category.item == "Regular Pizza"
            or item.category.item == "Sicilian Pizza"
        ):
            self.fields["toppings"].queryset = Topping.objects.filter(category="Pizza")
        elif item.category.item == "Sub" and item.item == "Steak + Cheese":
            self.fields["toppings"].queryset = Topping.objects.filter(
                Q(category="Steak+Cheese") | Q(category="Sub")
            )
        elif item.category.item == "Sub":
            self.fields["toppings"].queryset = Topping.objects.filter(category="Sub")
        else:
            del self.fields["toppings"]
