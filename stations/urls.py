from django.contrib import admin
from django.urls import path

from .views import index, StationListView, StationDetailView, FuelListView

urlpatterns = [
    path("", index, name="index"),
    path("stations/", StationListView.as_view(), name="station-list"),
    path("stations/<int:pk>/", StationDetailView.as_view(), name="station-detail"),
    path("fuel/", FuelListView.as_view(), name="fuel-list")
]

app_name = "stations"