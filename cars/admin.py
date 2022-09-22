from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Car Image'
    list_display = ('id','thumbnail', 'car_title', 'color', 'model', 'body_style', 'fuel_type', 'is_featured')
    search_fields = ('id', 'car_title', 'color', 'model', 'body_style', 'fuel_type')
    list_filter = ( 'color', 'model', 'fuel_type')
admin.site.register(Car, CarAdmin)
