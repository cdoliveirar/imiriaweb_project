from django.contrib import admin
from .models import BusinessType
#from .models import EnterpriseBusiness
	
'''
class EnterpriceBusinessAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name',)

admin.site.register(EnterpriseBusiness,EnterpriceBusinessAdmin)
'''

class BusinessTypeAdmin(admin.ModelAdmin):
	list_display = ('business_type_name','created_at',)

admin.site.register(BusinessType,BusinessTypeAdmin)	