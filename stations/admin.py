from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from stations.models import Manager, Fuel, Station, Transaction, Discount


admin.site.register(Fuel)
admin.site.register(Station)
admin.site.register(Transaction)
admin.site.register(Discount)
admin.site.register(Manager, UserAdmin)
