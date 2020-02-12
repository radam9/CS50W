from django import forms
from orders.models import OrderItem, Topping


class CreateOrderItem(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ["toppings", "size", "quantity"]
        widgets = {
            "toppings": forms.CheckboxSelectMultiple(),
            "size": forms.RadioSelect(),
            "quantity": forms.NumberInput(
                attrs={"value": 1, "min": 1, "max": 25, "step": 1}
            ),
        }
