from __future__ import annotations
import pathlib
import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

from config import settings


def image_upload_handler(instance: Station, filename: str) :
	fpath=pathlib.Path(filename)
	new_fname=str(uuid.uuid1())
	return f'station-images/{new_fname}{fpath.suffix}'


class Manager(AbstractUser):
    class Meta:
        verbose_name = "manager"
        verbose_name_plural = "managers"

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"


class Fuel(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False)
    price = models.DecimalField(null=False, decimal_places=2, max_digits=50)

    class Meta:
        verbose_name = "fuel"
        verbose_name_plural = "fuel"
        ordering = ["price",]
    
    def __str__(self) -> str:
        return f"{self.name}: {self.price}$\litre"


class Station(models.Model):
    address = models.CharField(max_length=255, null=False)
    managers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="stations")
    image = models.ImageField(upload_to = image_upload_handler, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.address}"        


class Discount(models.Model):
    description = models.CharField(max_length=255, null=False)
    discount = models.DecimalField(null=False, decimal_places=2, max_digits=4, validators=[MinValueValidator(0.01), MaxValueValidator(99.99)])
    is_active = models.BooleanField(null=True)

    class Meta:
        ordering = ["discount",]

    def __str__(self) -> str:
        return f"{self.discount}$: {self.description}"
    


class Transaction(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=False)
    fuel = models.ForeignKey(Fuel, on_delete=models.SET_NULL, null=True, related_name="transactions",)
    amount = models.DecimalField(null=False, decimal_places=2, max_digits=50)
    station = models.ForeignKey(Station, on_delete=models.DO_NOTHING, null=False, related_name="transactions")
    total = models.DecimalField(decimal_places=2, max_digits=50, null=True)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, related_name="transactions")
    discount_total = models.DecimalField(decimal_places=2, max_digits=50, null=True, default=None)

    class Meta:
        ordering = ["-date",]
    
    def __str__(self) -> str:
        return f"{self.date}: total {self.total}$|{self.fuel.name}"

    def save(self, *args, **kwargs) -> None:
        self.total = (self.amount * self.fuel.price)
        if self.discount_total is None:
            if self.discount and self.discount.is_active:
                self.discount_total = self.total * (self.discount.discount / 100)
                self.total -= self.discount_total
            else:
                self.discount_total = 0
        super(Transaction, self).save(*args, **kwargs)
