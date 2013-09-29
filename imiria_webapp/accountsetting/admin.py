from django.contrib import admin
from .models import Country, EnterpriseBusiness


class EnterpriceBusinessAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','logo')

admin.site.register(EnterpriseBusiness, EnterpriceBusinessAdmin)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name',)
    
admin.site.register(Country, CountryAdmin)

