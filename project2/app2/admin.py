from django.contrib import admin
from .models import EA

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("AA", "BA", "DA", "TA",)
  
admin.site.register(EA, MemberAdmin)