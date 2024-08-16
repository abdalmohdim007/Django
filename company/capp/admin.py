from django.contrib import admin
from .models import companydb

# Register your models here.


class MemberAdmin(admin.ModelAdmin):
  list_display = ("company", "department", "employeeID","employee_lastname", "birthdate", "vacations","used_vacations", "salary", )
   

admin.site.register(companydb, MemberAdmin)