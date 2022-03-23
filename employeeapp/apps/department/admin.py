from django.contrib import admin
from .models import Department

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    '''Admin View for Department'''

    list_display = ('name', 'short_name', 'active',)
    list_filter = ('active',)
    search_fields = ('short_name',)
    list_per_page = 20
