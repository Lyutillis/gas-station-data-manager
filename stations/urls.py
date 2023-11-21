from django.contrib import admin
from django.urls import path

from .views import StationListView, StationDetailView

urlpatterns = [
    path("", StationListView.as_view(), name="station-list"),
    path("stations/<pk>", StationDetailView.as_view(), name="station-detail"),
]

app_name = "stations"