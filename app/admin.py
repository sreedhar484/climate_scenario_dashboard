from django.contrib import admin
from .models import corban_pricing,economic_forecast,co2_emission,energy_cost

admin.site.register(corban_pricing)
admin.site.register(economic_forecast)
admin.site.register(co2_emission)
admin.site.register(energy_cost)
