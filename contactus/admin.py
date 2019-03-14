from django.contrib import admin
from . models import Company, Branch, CustomerServiceHours, CompanyHQ, Message


admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(CustomerServiceHours)
admin.site.register(CompanyHQ)
admin.site.register(Message)