from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView

from stations.forms import ManagerLoginForm, ManagerCreationForm, StationForm, ManagerUsernameSearchForm, DiscountDescriptionSearchForm, FuelNameSearchForm, StationAddressSearchForm, ManagerUpdateForm
from stations.models import Station, Fuel, Discount, Manager, Transaction


def index(request):
    context = {
        "stations": Station.objects.count(),
        "managers": Manager.objects.count(),
        "transactions": Transaction.objects.count(),
    }
    return render(request, "stations/index.html", context=context)


class StationListView(ListView):
    model = Station
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs) -> dict[str, Any]:
        context = super(StationListView, self).get_context_data(**kwargs)
        address = self.request.GET.get("address", "")
        context["search_form"] = StationAddressSearchForm(
            initial={"address": address}
        )
        return context

    def get_queryset(self):
        form = StationAddressSearchForm(self.request.GET)
        self.queryset = self.model.objects.filter(managers=self.request.user.pk)
        
        if form.is_valid():
            return self.queryset.filter(address__icontains=form.cleaned_data["address"])

        return self.queryset


class StationDetailView(DetailView):
    model = Station


class StationCreateView(CreateView):
    model = Station
    fields = ("address", "image", "managers",)
    success_url = reverse_lazy("stations:station-list")


class StationUpdateView(UpdateView):
    model = Station
    form_class = StationForm
    success_url = reverse_lazy("stations:station-list")


class StationDeleteView(DeleteView):
    model = Station
    success_url = reverse_lazy("stations:station-list")



class FuelListView(ListView):
    model = Fuel
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs) -> dict[str, Any]:
        context = super(FuelListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = FuelNameSearchForm(
            initial={"name": name}
        )
        return context
    
    def get_queryset(self):
        form = FuelNameSearchForm(self.request.GET)
        self.queryset = self.model.objects.all()
        
        if form.is_valid():
            return self.queryset.filter(name__icontains=form.cleaned_data["name"])

        return self.queryset


class FuelDetailView(DetailView):
    model = Fuel


class FuelCreateView(CreateView):
    model = Fuel
    fields = ("name", "price",)
    success_url = reverse_lazy("stations:fuel-list")


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
    queryset = Discount.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs) -> dict[str, Any]:
        context = super(DiscountListView, self).get_context_data(**kwargs)
        description = self.request.GET.get("description", "")
        context["search_form"] = DiscountDescriptionSearchForm(
            initial={"description": description}
        )
        return context
    
    def get_queryset(self):
        form = DiscountDescriptionSearchForm(self.request.GET)
        self.queryset = self.model.objects.all()
        
        if form.is_valid():
            return self.queryset.filter(description__icontains=form.cleaned_data["description"])

        return self.queryset


class DiscountCreateView(CreateView):
    model = Discount
    fields = ("description", "discount", "is_active",)
    success_url = reverse_lazy("stations:discount-list")


class DiscountDetailView(DetailView):
    model = Discount


class DiscountUpdateView(UpdateView):
    model = Discount
    fields = ("description", "discount", "is_active",)
    success_url = reverse_lazy("stations:discount-list")


class DiscountDeleteView(DeleteView):
    model = Discount
    success_url = reverse_lazy("stations:discount-list")


class ManagerCreateView(CreateView):
    model = Manager
    form_class = ManagerCreationForm
    success_url = reverse_lazy("stations:manager-list")
    template_name = "registration/register.html"


class ManagerListView(ListView):
    model = Manager
    paginate_by = 6
    queryset = Manager.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs) -> dict[str, Any]:
        context = super(ManagerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = ManagerUsernameSearchForm(
            initial={"username": username}
        )
        return context
    
    def get_queryset(self):
        form = ManagerUsernameSearchForm(self.request.GET)
        self.queryset = self.model.objects.all()
        
        if form.is_valid():
            return self.queryset.filter(username__icontains=form.cleaned_data["username"])

        return self.queryset


class ManagerDetailView(DetailView):
    model = Manager


class ManagerLoginView(LoginView):
    template_name = "registration/login.html"
    form_class = ManagerLoginForm
    success_url = reverse_lazy("stations:station-list")


class ManagerUpdateView(UpdateView):
    model = Manager
    form_class = ManagerUpdateForm
    success_url = reverse_lazy("stations:manager-list")
