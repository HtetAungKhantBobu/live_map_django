from django.shortcuts import render
from property_manager.models import Property
import json
from helpers import helpers
from django.db.models import F


def hello(request):
    queryset = (
        Property.objects.all()
        .order_by("-created_at")
        .annotate(township_name=F("township__name"), type_name=F("type__name"))
        .values(
            "id",
            "address",
            "township_name",
            "type_name",
            "price",
            "lat",
            "long",
            "is_available",
            "is_rent",
            "created_at",
        )
    )
    test_queryset = Property.objects.all().select_related("type.name", "township.name")
    context = {
        "property_list": queryset,
        "test": "test",
        "property_list_json": json.dumps(list(queryset), cls=helpers.UUIDEncoder),
    }
    return render(request, "property_manager/index.html", context=context)


# Create your views here.
