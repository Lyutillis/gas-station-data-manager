from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from stations.models import Station, Manager


class StationForm(forms.ModelForm):
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Address",
                "class": "form-control"
            }
        ))
    managers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "placeholder": "Image",
                "class": "form-control",
            }
        )
    )

    class Meta:
        model = Station
        fields = ["address", "image", "managers",]


class ManagerLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    
    class Meta:
        model = get_user_model()
        fields = ("username", "password",)


class ManagerCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', "first_name", "last_name", 'password1', 'password2')


class ManagerUsernameSearchForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username",
                "class": "form-control",

            }
        ),
    )


class FuelNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=150,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by Fuel Type",
                "class": "form-control",
            }
        )
    )


class StationAddressSearchForm(forms.Form):
    address = forms.CharField(
        max_length=150,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by Address",
                "class": "form-control",
            }
        )
    )


class DiscountDescriptionSearchForm(forms.Form):
    description = forms.CharField(
        max_length=150,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by description",
                "class": "form-control",
            }
        )
    )


class ManagerUpdateForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ["username", "first_name", "last_name",]
