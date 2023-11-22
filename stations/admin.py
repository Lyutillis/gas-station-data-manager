from django.contrib import admin

from stations.models import Fuel, Station, Transaction, Discount


admin.site.register(Fuel)
admin.site.register(Station)
admin.site.register(Transaction)
admin.site.register(Discount)
