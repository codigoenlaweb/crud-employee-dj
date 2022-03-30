from django import forms
from apps.department.models import Department
from .models import Employee

class EmployeeForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label='Department select')
    
    class Meta:
        model = Employee
        fields = '__all__'
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'bg-gray-200 rounded px-2 py-1 text-gray-500 outline-color-primary mb-3 mt-3 md:mt-4 md:mb-4 w-full max-w-xs', 'placeholder': 'First name'})
        self.fields['last_name'].widget.attrs.update({'class': 'bg-gray-200 rounded px-2 py-1 text-gray-500 outline-color-primary mb-3 md:mb-4 w-full max-w-xs', 'placeholder': 'Last name'})
        self.fields['job'].widget.attrs.update({'class': 'bg-gray-200 rounded px-2 py-1 text-gray-500 outline-color-primary mb-3 md:mb-4 w-full max-w-xs', 'placeholder': 'Job'})
        self.fields['department'].widget.attrs.update({'class': 'bg-gray-200 rounded px-2 py-1 text-gray-500 outline-color-primary mb-3 md:mb-4 w-full max-w-xs'})
        self.fields['avatar'].widget.attrs.update({'class': 'bg-gray-200 rounded block text-gray-500 outline-color-primary mb-3 md:mb-4 w-full max-w-xs border border-gray-300'})