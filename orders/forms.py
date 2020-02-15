from django import forms
from django.db.models import Q
from orders.models import OrderItem, Topping, Menu


class CreateOrderItem(forms.ModelForm):

    item = forms.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = OrderItem
        exclude = []
        fields = ["size", "quantity"]
        widgets = {
            "item": forms.HiddenInput(),
            "size": forms.RadioSelect(),
            "quantity": forms.NumberInput(
                attrs={"value": 1, "min": 1, "max": 25, "step": 1}
            ),
        }

    def __init__(self, *args, **kwargs):
        if "x" in kwargs:
            i = kwargs.pop("x")
            item = Menu.objects.get(id=i)

            super(CreateOrderItem, self).__init__(*args, **kwargs)
            if (
                item.category.item == "Regular Pizza"
                or item.category.item == "Sicilian Pizza"
            ) and (item.item != "Cheese"):
                self.fields["toppings"] = forms.ModelMultipleChoiceField(
                    queryset=Topping.objects.filter(category="Pizza"),
                    widget=forms.SelectMultiple(),
                )
            elif item.item == "Steak + Cheese":
                self.fields["toppings"] = forms.ModelMultipleChoiceField(
                    queryset=Topping.objects.filter(
                        Q(category="Steak+Cheese") | Q(category="Sub")
                    ),
                    widget=forms.SelectMultiple(),
                    required=False,
                )
            elif item.category.item == "Sub":
                self.fields["toppings"] = forms.ModelMultipleChoiceField(
                    queryset=Topping.objects.filter(category="Sub"),
                    widget=forms.SelectMultiple(),
                    required=False,
                )

            # modifying the size field depending on the menu item
            if (
                item.category.item == "Pasta"
                or item.category.item == "Salad"
                or item.item == "Sausage, Peppers & Onions"
            ):
                self.fields["size"].choices = [("l", "Large")]

            def clean_toppings(self):
                toppings = self.cleaned_data["toppings"]
                item_id = self.cleaned_data["item"]
                menuitem = Menu.objects.get(id=item_id)
                if len(toppings) > menuitem.tops:
                    raise forms.ValidationError("You have selected too many toppings")
                if (
                    menuitem.category.item == "Regular Pizza"
                    or menuitem.category.item == "Sicilian Pizza"
                ) and (menuitem.item != "Cheese"):
                    if len(toppings) != menuitem.tops:
                        raise forms.ValidationError(
                            "You have selected to little toppings"
                        )
                return toppings

        else:
            super(CreateOrderItem, self).__init__(*args, **kwargs)

    # def __init__(self, *args, **kwargs):
    #     if "x" in kwargs:
    #         i = kwargs.pop("x")
    #         item = Menu.objects.get(id=i)

    #         super(CreateOrderItem, self).__init__(*args, **kwargs)
    #         # modifying the topping field depending on the menu item
    #         if (
    #             item.category.item == "Regular Pizza"
    #             or item.category.item == "Sicilian Pizza"
    #         ) and (item.item != "Cheese"):
    #             self.fields["toppings"].queryset = Topping.objects.filter(
    #                 category="Pizza"
    #             )
    #         elif item.item == "Steak + Cheese":
    #             self.fields["toppings"].queryset = Topping.objects.filter(
    #                 Q(category="Steak+Cheese") | Q(category="Sub")
    #             )
    #         elif item.category.item == "Sub":
    #             self.fields["toppings"].queryset = Topping.objects.filter(
    #                 category="Sub"
    #             )
    #         else:
    #             self.base_fields.pop("toppings")

    #         # modifying the size field depending on the menu item
    #         if (
    #             item.category.item == "Pasta"
    #             or item.category.item == "Salad"
    #             or item.item == "Sausage, Peppers & Onions"
    #         ):
    #             self.fields["size"].choices = [("l", "Large")]
    #     else:
    #         super(CreateOrderItem, self).__init__(*args, **kwargs)

