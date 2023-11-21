from django.contrib import admin

from stations.models import Fuel, Station, Discount, Transaction


admin.site.register(Fuel)
admin.site.register(Station)
admin.site.register(Discount)
admin.site.register(Transaction)