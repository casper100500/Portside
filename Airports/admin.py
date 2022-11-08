from django.contrib import admin
from Airports.models import Airport
# Register your models here.


class AirportAdmin(admin.ModelAdmin):
    #readonly_fields=('slug',)
    #prepopulated_fields={'slug':('title',)}
    list_filter = ('type','scheduled_service','continent')
    list_display = ('ident','name','type','iso_region')
    search_fields = ['ident','name']
admin.site.register(Airport,AirportAdmin)