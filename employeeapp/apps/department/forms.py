from django import forms
from apps.department.models import Department

class DepartmentAndEmployeeForm(forms.Form):
    # Deparment
    department_name = forms.CharField(max_length=50, min_length=5)
    department_short_name = forms.CharField(max_length=20, min_length=3)
    
    # Employee
    employee_first_name = forms.CharField(max_length=32, min_length=3)
    employee_last_name = forms.CharField(max_length=32, min_length=3)
    employee_job = forms.CharField(max_length=50, min_length=3)
    employee_avatar = forms.ImageField(required=False)
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department_name'].widget.attrs.update({'class': 'bg-gray-200 rounded px-2 py-1 text-gray-500 outline-color-primary mb-3 mt-3 md:mt-4 md:mb-4 w-full max-w-xs', 'placeholder': 'department name'})
        self.fields['department_short_name'].widget.attrs.update({'class': 'bg-gray-200 rounded px-2 py-1 text-gray-500 outline-color-primary mb-3 md:mb-4 w-full max-w-xs', 'placeholder': 'department short name'})
        self.fields['employee_first_name'].widget.attrs.update({'class': 'bg-gray-200 rounded px-2 py-1 text-gray-500 outline-color-primary mb-3 mt-3 md:mt-4 md:mb-4 w-full max-w-xs', 'placeholder': 'First name'})
        self.fields['employee_last_name'].widget.attrs.update({'class': 'bg-gray-200 rounded px-2 py-1 text-gray-500 outline-color-primary mb-3 md:mb-4 w-full max-w-xs', 'placeholder': 'Last name'})
        self.fields['employee_job'].widget.attrs.update({'class': 'bg-gray-200 rounded px-2 py-1 text-gray-500 outline-color-primary mb-3 md:mb-4 w-full max-w-xs', 'placeholder': 'Job'})
        self.fields['employee_avatar'].widget.attrs.update({'class': 'bg-gray-200 rounded block text-gray-500 outline-color-primary mb-3 md:mb-4 w-full max-w-xs border border-gray-300'})
        
        
class DepartmentForm(forms.ModelForm):
    name = forms.CharField(max_length=32, min_length=3)
    short_name = forms.CharField(max_length=32, min_length=3)
    
    
    
    class Meta:
        model = Department
        fields = '__all__'
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'bg-gray-200 rounded px-2 py-1 text-gray-500 outline-color-primary mb-3 mt-3 md:mt-4 md:mb-4 w-full max-w-xs', 'placeholder': 'First name'})
        self.fields['short_name'].widget.attrs.update({'class': 'bg-gray-200 rounded px-2 py-1 text-gray-500 outline-color-primary mb-3 md:mb-4 w-full max-w-xs', 'placeholder': 'Last name'})
        self.fields['active'].widget.attrs.update({'class': 'w-5 h-5 rounded outline-color-primary mb-3 md:mb-4'})