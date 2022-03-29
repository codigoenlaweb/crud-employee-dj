from django.views.generic import ListView, DetailView
from .models import Employee
# Create your views here.

class EmployeeListView(ListView):
    context_object_name = 'employee'
    template_name = "employee/list-employee.html"
    paginate_by = 20
    
    def get_queryset(self):
        employee_get = self.request.GET.get("filter")
        
        if employee_get == None:
            employee_get = ''
            
        queryset = Employee.objects.filter(first_name__contains=employee_get).order_by("-id")
        return queryset
    
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['filter'] = self.request.GET.get("filter")
        return context
    
    

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "employee/show-employee.html"
    context_object_name = 'employee'
    

    
