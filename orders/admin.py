from django.contrib import admin
from .models import Menu, Order, Topping, Category


class MenuInline(admin.TabularInline):
    model = Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ["id", "item", "category", "sprice", "lprice"]
    search_fields = ["item", "category"]
    list_filter = ["category"]
    list_editable = ["item", "category", "sprice", "lprice"]
    list_display_links = ["id"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "total", "status"]
    search_fields = ["user", "total", "status"]
    list_filter = ["status"]
    list_editable = ["status"]
    list_display_links = ["id"]


class ToppingAdmin(admin.ModelAdmin):
    list_display = ["id", "item", "category", "price"]
    list_editable = ["item", "category", "price"]
    list_filter = ["category"]
    list_display_links = ["id"]


class CategoryAdmin(admin.ModelAdmin):
    inlines = [MenuInline]
    list_display = ["id", "item"]
    list_editable = ["item"]
    list_display_links = ["id"]


admin.site.register(Menu, MenuAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(Category, CategoryAdmin)
