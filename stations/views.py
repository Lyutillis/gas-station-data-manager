from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView

from stations.models import Station


class StationListView(ListView):
    model = Station
    context_object_name = "station_list"
    template_name = "station/station_list.html"
    paginate_by = 4


class StationDetailView(DetailView):
    model = Station

