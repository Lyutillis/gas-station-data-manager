from __future__ import annotations
import pathlib
import uuid
from django.db import models
from config import settings


def image_upload_handler(instance: Station, filename: str) :
	fpath=pathlib.Path(filename)
	new_fname=str(uuid.uuid1())
	return f'station-images/{instance.id}/{new_fname}{fpath.suffix}'


class Fuel(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False)
    price = models.DecimalField(null=False, decimal_places=2, max_digits=50)


class Station(models.Model):
    address = models.CharField(max_length=255, null=False)
    managers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="stations")
    image = models.ImageField(upload_to = image_upload_handler, null=True, blank=True)


class Discount(models.Model):
    description = models.CharField(max_length=255, null=False)
    discount = models.DecimalField(decimal_places=2, null=False, max_digits=5)
    is_active = models.BooleanField()


class Transaction(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=False)
    fuel = models.ForeignKey(Fuel, on_delete=models.DO_NOTHING, null=False, related_name="transactions")
    amount = models.DecimalField(null=False, decimal_places=2, max_digits=50)
    station = models.ForeignKey(Station, on_delete=models.DO_NOTHING, null=False, related_name="transactions")
    discount = models.ForeignKey(Discount, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="transactions")
    total = models.DecimalField(null=False, decimal_places=2, max_digits=50)

    class Meta:
         ordering = ("date", )

    def save(self, *args, **kwargs) -> None:
        self.total = self.amount * self.fuel.price
        super(Transaction, self).save(*args, **kwargs)