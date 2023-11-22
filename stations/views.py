from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from stations.models import Station, Fuel, Discount


def index(request):
    return render(request, "stations/index.html")


class StationListView(ListView):
    model = Station
    paginate_by = 4


class StationDetailView(DetailView):
    model = Station


class StationUpdateView(UpdateView):
    model = Station
    fields = ("address", "image", "managers")
    success_url = reverse_lazy("stations:station-list")


class StationDeleteView(DeleteView):
    model = Station
    success_url = reverse_lazy("stations:station-list")


class FuelListView(ListView):
    model = Fuel
    paginate_by = 6


class FuelDetailView(DetailView):
    model = Fuel


class FuelUpdateView(UpdateView):
    model = Fuel
    fields = ("name", "price",)
    success_url = reverse_lazy("stations:fuel-list")


class FuelDeleteView(DeleteView):
    model = Fuel
    success_url = reverse_lazy("stations:fuel-list")


class DiscountListView(ListView):
    model = Discount
    paginate_by = 6


class DiscountDetailView(DetailView):
    model = Discount


class DiscountUpdateView(UpdateView):
    model = Discount
    fields = ("description", "discount", "is_active",)
    success_url = reverse_lazy("stations:discount-list")


class DiscountDeleteView(DeleteView):
    model = Discount
    success_url = reverse_lazy("stations:discount-list")
