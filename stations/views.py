from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash

from stations.forms import (
    StationForm,
    StationAddressSearchForm,
    FuelForm,
    FuelNameSearchForm,
    DiscountForm,
    DiscountDescriptionSearchForm,
    ManagerLoginForm,
    ManagerCreationForm,
    ManagerUpdateForm,
    ManagerUsernameSearchForm,
    TransactionForm,
)
from stations.models import Station, Fuel, Discount, Manager, Transaction


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "stations": Station.objects.count(),
        "managers": Manager.objects.count(),
        "transactions": Transaction.objects.count(),
    }
    return render(request, "stations/index.html", context=context)


class StationListView(LoginRequiredMixin, ListView):
    model = Station
    paginate_by = 6

    def get_context_data(
        self,
        *,
        object_list=None,
        **kwargs
    ) -> dict[str, Any]:
        context = super(StationListView, self).get_context_data(**kwargs)
        address = self.request.GET.get("address", "")
        context["search_form"] = StationAddressSearchForm(
            initial={"address": address}
        )
        return context

    def get_queryset(self) -> QuerySet:
        form = StationAddressSearchForm(self.request.GET)
        self.queryset = self.model.objects.prefetch_related()
        if not self.request.user.is_staff:
            self.queryset = self.queryset.filter(
                managers=self.request.user.pk
            )

        if form.is_valid():
            return self.queryset.filter(
                address__icontains=form.cleaned_data["address"]
            )

        return self.queryset


class StationDetailView(LoginRequiredMixin, DetailView):
    model = Station


class StationCreateView(LoginRequiredMixin, CreateView):
    model = Station
    form_class = StationForm
    success_url = reverse_lazy("stations:station-list")


class StationUpdateView(LoginRequiredMixin, UpdateView):
    model = Station
    form_class = StationForm
    success_url = reverse_lazy("stations:station-list")


class StationDeleteView(LoginRequiredMixin, DeleteView):
    model = Station
    success_url = reverse_lazy("stations:station-list")


class FuelListView(LoginRequiredMixin, ListView):
    model = Fuel
    paginate_by = 6

    def get_context_data(
        self,
        *,
        object_list=None,
        **kwargs
    ) -> dict[str, Any]:
        context = super(FuelListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = FuelNameSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self) -> QuerySet:
        form = FuelNameSearchForm(self.request.GET)
        self.queryset = self.model.objects.all()

        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )

        return self.queryset


class FuelDetailView(LoginRequiredMixin, DetailView):
    model = Fuel


class FuelCreateView(LoginRequiredMixin, CreateView):
    model = Fuel
    form_class = FuelForm
    success_url = reverse_lazy("stations:fuel-list")


class FuelUpdateView(LoginRequiredMixin, UpdateView):
    model = Fuel
    form_class = FuelForm
    success_url = reverse_lazy("stations:fuel-list")


class FuelDeleteView(LoginRequiredMixin, DeleteView):
    model = Fuel
    success_url = reverse_lazy("stations:fuel-list")


class DiscountListView(LoginRequiredMixin, ListView):
    model = Discount
    paginate_by = 6

    def get_context_data(
        self,
        *,
        object_list=None,
        **kwargs
    ) -> dict[str, Any]:
        context = super(DiscountListView, self).get_context_data(**kwargs)
        description = self.request.GET.get("description", "")
        context["search_form"] = DiscountDescriptionSearchForm(
            initial={"description": description}
        )
        return context

    def get_queryset(self) -> QuerySet:
        form = DiscountDescriptionSearchForm(self.request.GET)
        self.queryset = self.model.objects.all()

        if form.is_valid():
            return self.queryset.filter(
                description__icontains=form.cleaned_data["description"]
            )

        return self.queryset


class DiscountCreateView(LoginRequiredMixin, CreateView):
    model = Discount
    form_class = DiscountForm
    success_url = reverse_lazy("stations:discount-list")


class DiscountDetailView(LoginRequiredMixin, DetailView):
    model = Discount


class DiscountUpdateView(LoginRequiredMixin, UpdateView):
    model = Discount
    form_class = DiscountForm
    success_url = reverse_lazy("stations:discount-list")


class DiscountDeleteView(LoginRequiredMixin, DeleteView):
    model = Discount
    success_url = reverse_lazy("stations:discount-list")


class ManagerCreateView(LoginRequiredMixin, CreateView):
    model = Manager
    form_class = ManagerCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("stations:manager-list")


class ManagerListView(LoginRequiredMixin, ListView):
    model = Manager
    paginate_by = 6

    def get_context_data(
        self,
        *,
        object_list=None,
        **kwargs
    ) -> dict[str, Any]:
        context = super(ManagerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = ManagerUsernameSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self) -> QuerySet:
        form = ManagerUsernameSearchForm(self.request.GET)
        self.queryset = self.model.objects.prefetch_related().all()
        if form.is_valid():
            return self.queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )

        return self.queryset


class ManagerDetailView(LoginRequiredMixin, DetailView):
    model = Manager


class ManagerLoginView(LoginView):
    template_name = "registration/login.html"
    form_class = ManagerLoginForm


class ManagerUpdateView(LoginRequiredMixin, UpdateView):
    model = Manager
    form_class = ManagerUpdateForm
    success_url = reverse_lazy("stations:manager-list")


class ManagerDeleteView(LoginRequiredMixin, DeleteView):
    model = Manager
    success_url = reverse_lazy("stations:manager-list")


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = "stations/transaction_form.html"
    success_url = reverse_lazy("stations:transaction-list")

    def get_success_url(self) -> str:
        station_id = self.object.station.id
        return reverse_lazy("stations:station-detail", kwargs={"pk": station_id})


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy("stations:transaction-list")

    def get_success_url(self) -> str:
        station_id = self.object.station.id
        return reverse_lazy("stations:station-detail", kwargs={"pk": station_id})


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    success_url = reverse_lazy("stations:transaction-list")

    def get_success_url(self) -> str:
        station_id = self.object.station.id
        return reverse_lazy("stations:station-detail", kwargs={"pk": station_id})


class ManagerPasswordChangeView(PasswordChangeView):
    template_name = "registration/change_password.html"
    success_url = reverse_lazy("stations:manager-list")

    def form_valid(self, form):
        response = super().form_valid(form)
        update_session_auth_hash(self.request, form.user)
        return response
