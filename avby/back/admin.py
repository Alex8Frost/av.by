from django.contrib import admin
from back.models import TransportModel, TransportMark, TransportAd
from django.conf import settings


@admin.register(TransportModel)
class TransportModelAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'mark']
    list_filter = ['name', 'mark']


@admin.register(TransportMark)
class TransportMarkAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_filter = ['name', ]


@admin.register(TransportAd)
class TransportAdAdmin(admin.ModelAdmin):
    list_display = ['mark', 'model', 'type_of_transport', 'year', 'price_in_dollar', 'engine', 'engine_capacity',
                    'drive_unit', 'mileage', 'vin_number', 'status', 'description', 'post_date', 'close_date']
    list_filter = ['mark', 'model', 'year', 'price_in_dollar', 'mileage', 'status',  'post_date', 'close_date']

