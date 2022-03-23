from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    '''Admin View for Employee'''

    list_display = ('full_name', 'employee_department', 'job',)
    list_filter = ('department',)
    search_fields = ('first_name', 'last_name',)
    list_per_page = 20
    # ordering = ('',)

    def full_name(self, obj) -> str:
        return f'{obj.first_name} {obj.last_name}'
    
    def employee_department(self, obj) -> str:
        return f'{obj.department.name}'
