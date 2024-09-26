from typing import Any
from django.contrib import admin
from property_manager.models import Township, PropertyType, Property


@admin.register(Township)
class TownshipAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["id", "name"]


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["id", "name"]


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "type",
        "township",
        "address",
        "is_available",
        "added_by",
        "created_at",
        "updated_at",
    ]

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        if not change:
            obj.added_by = request.user
        return super().save_model(request, obj, form, change)


# Register your models here.
