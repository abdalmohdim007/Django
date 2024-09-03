from django.contrib import admin
from .models import Task, ToDoList, Contact

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'creation_date', 'start_date', 'finish_date', 'due_date', 'status', 'category')
    list_filter = ('status', 'category', 'creation_date')
    search_fields = ('name', 'description')
    date_hierarchy = 'creation_date'
    ordering = ('-creation_date',)

class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'description')
    search_fields = ('name', 'description')
  #  filter_horizontal = ('tasks',)  # Makes the many-to-many relationship easier to manage

class ContactAdmin(admin.ModelAdmin):
  list_display = ("name", "email")  

admin.site.register(Task, TaskAdmin)
admin.site.register(ToDoList, ToDoListAdmin)
admin.site.register(Contact, ContactAdmin)
