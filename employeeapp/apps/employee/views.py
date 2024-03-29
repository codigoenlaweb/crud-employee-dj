from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Employee
from .forms import EmployeeForm
# Create your views here.


class EmployeeListView(ListView):
    context_object_name = 'employee'
    template_name = "employee/list-employee.html"
    paginate_by = 20

    def get_queryset(self):
        employee_get = self.request.GET.get("filter")

        if employee_get == None:
            employee_get = ''

        queryset = Employee.objects.filter(
            first_name__contains=employee_get).order_by("-id")
        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['filter'] = self.request.GET.get("filter")

        # if filter is none change for ''
        if context['filter'] == None:
            context['filter'] = ''

        return context


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "employee/show-employee.html"
    context_object_name = 'employee'


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "employee/create-employee.html"
    form_class = EmployeeForm
    success_url = reverse_lazy('employee:employeeList')


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = "employee/update-employee.html"
    form_class = EmployeeForm

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        employee = form.save()
        self.success_url = reverse_lazy(
            'employee:employeeshow', args=[employee.id])
        return super().form_valid(form)


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "employee/delete-employee.html"
    success_url = reverse_lazy('employee:employeeList')
