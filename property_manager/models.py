from django.db import models
import uuid
from users.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


class PropertyType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("name of the type", unique=True, max_length=256)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Township(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("name of the township", unique=True, max_length=256)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Property(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    price = models.PositiveBigIntegerField(
        "Monthly Price/Sale Price", blank=True, null=True
    )
    lat = models.CharField("Latitude", max_length=256, blank=True, null=True)
    long = models.CharField("Longtitude", max_length=256, blank=True, null=True)
    type = models.ForeignKey(
        PropertyType, blank=True, null=True, on_delete=models.CASCADE
    )
    address = models.TextField("Address of the property", blank=True, null=True)
    township = models.ForeignKey(
        Township, blank=True, null=True, on_delete=models.CASCADE
    )
    is_available = models.BooleanField("Is this property available", default=True)
    is_rent = models.BooleanField(
        "Is this property being rented, or sold?", default=True
    )
    misc = models.JSONField("Other details in JSON format", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
