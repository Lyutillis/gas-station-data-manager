from django.contrib.auth.forms import UserCreationForm

from stations.models import Manager


class ManagerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Manager
