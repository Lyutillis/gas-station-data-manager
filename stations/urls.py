from django.contrib import admin
from django.urls import path

from .views import (
    index,
    StationListView,
    StationDetailView,
    StationUpdateView,
    FuelListView,
    StationDeleteView,
    FuelDetailView,
    FuelUpdateView,
    FuelDeleteView,
    DiscountListView,
    DiscountDetailView,
    DiscountUpdateView,
    DiscountDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("stations/", StationListView.as_view(), name="station-list"),
    path("stations/<int:pk>/", StationDetailView.as_view(), name="station-detail"),
    path("stations/update/<int:pk>/", StationUpdateView.as_view(), name="station-update"),
    path("stations/delete/<int:pk>/", StationDeleteView.as_view(), name="station-delete"),
    path("fuel/", FuelListView.as_view(), name="fuel-list"),
    path("fuel/<int:pk>/", FuelDetailView.as_view(), name="fuel-detail"),
    path("fuel/update/<int:pk>/", FuelUpdateView.as_view(), name="fuel-update"),
    path("fuel/delete/<int:pk>/", FuelDeleteView.as_view(), name="fuel-delete"),
    path("discount/", DiscountListView.as_view(), name="discount-list"),
    path("discount/<int:pk>/", DiscountDetailView.as_view(), name="discount-detail"),
    path("discount/update/<int:pk>/", DiscountUpdateView.as_view(), name="discount-update"),
    path("discount/delete/<int:pk>/", DiscountDeleteView.as_view(), name="discount-delete"),
]

app_name = "stations"