from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView

from stations.models import Station, Fuel


class StationListView(ListView):
    model = Station
    paginate_by = 4


class StationDetailView(DetailView):
    model = Station


class FuelListView(ListView):
    model = Fuel
    paginate_by = 6
