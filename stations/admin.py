from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from stations.models import Manager, Fuel, Station, Transaction, Discount


@admin.register(Manager)
class ManagerAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "email",
                        "first_name",
                        "last_name",
                    )
                },
            ),
        )
    )


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ("discount", "description", "is_active",)
    search_fields = ("discount", "description",)
    list_filter = ("discount", "is_active",)


@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    list_display = ("name", "price",)
    search_fields = ("name", "price",)
    list_filter = ("price",)


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ("address", "image_tag", "managers_tag",)
    search_fields = ("address", "managers",)
    list_filter = ("managers",)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "station",
        "fuel",
        "amount",
        "discount",
        "discount_total",
        "total",
    )
    search_fields = (
        "date",
        "station",
        "fuel",
        "amount",
        "discount_total",
        "total"
    )
    list_filter = ("date", "station", "fuel", "discount",)
    exclude = ("discount_total", "total",)
