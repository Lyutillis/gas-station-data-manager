from django.urls import path

from .views import (
    index,
    StationListView,
    StationDetailView,
    StationCreateView,
    StationUpdateView,
    StationDeleteView,
    FuelListView,
    FuelCreateView,
    FuelUpdateView,
    FuelDeleteView,
    DiscountListView,
    DiscountCreateView,
    DiscountUpdateView,
    DiscountDeleteView,
    ManagerListView,
    ManagerDetailView,
    ManagerCreateView,
    ManagerLoginView,
    ManagerUpdateView,
    ManagerDeleteView,
)


urlpatterns = [
    path("", index, name="index"),
    path("accounts/login/", ManagerLoginView.as_view(), name="login"),
    path("stations/", StationListView.as_view(), name="station-list"),
    path(
        "stations/<int:pk>/",
        StationDetailView.as_view(),
        name="station-detail"
    ),
    path(
        "stations/create/",
        StationCreateView.as_view(),
        name="station-create"
    ),
    path(
        "stations/update/<int:pk>/",
        StationUpdateView.as_view(),
        name="station-update"
    ),
    path(
        "stations/delete/<int:pk>/",
        StationDeleteView.as_view(),
        name="station-delete"
    ),
    path("fuel/", FuelListView.as_view(), name="fuel-list"),
    path("fuel/create/", FuelCreateView.as_view(), name="fuel-create"),
    path(
        "fuel/update/<int:pk>/",
        FuelUpdateView.as_view(),
        name="fuel-update"
    ),
    path(
        "fuel/delete/<int:pk>/",
        FuelDeleteView.as_view(),
        name="fuel-delete"
    ),
    path(
        "discounts/",
        DiscountListView.as_view(),
        name="discount-list"
    ),
    path(
        "discounts/create/",
        DiscountCreateView.as_view(),
        name="discount-create"
    ),
    path(
        "discounts/update/<int:pk>/",
        DiscountUpdateView.as_view(),
        name="discount-update",
    ),
    path(
        "discounts/delete/<int:pk>/",
        DiscountDeleteView.as_view(),
        name="discount-delete",
    ),
    path("managers/", ManagerListView.as_view(), name="manager-list"),
    path(
        "managers/<int:pk>/",
        ManagerDetailView.as_view(),
        name="manager-detail"
    ),
    path(
        "managers/create/",
        ManagerCreateView.as_view(),
        name="manager-create"
    ),
    path(
        "managers/update/<int:pk>/",
        ManagerUpdateView.as_view(),
        name="manager-update"
    ),
    path(
        "managers/delete/<int:pk>/",
        ManagerDeleteView.as_view(),
        name="manager-delete",
    ),
]

app_name = "stations"
