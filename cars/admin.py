from django.contrib import admin

from cars.models import Car2
# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'make', 'year', 'color')
    list_filter = ('make', )
    search_fields = ('color', 'year')


admin.site.register(Car2, CarAdmin, )
