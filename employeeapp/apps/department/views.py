from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from .models import Department
from .forms import DepartmentAndEmployeeForm
from apps.employee.models import Employee


class DepartmentListView(ListView):
    template_name = "department/list-department.html"
    context_object_name = 'department'
    paginate_by = 20

    def get_queryset(self):
        department_get = self.request.GET.get("filter")

        if department_get == None:
            department_get = ''

        queryset = Department.objects.filter(
            name__contains=department_get).order_by("-id")
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


class DepartmentCreateView(FormView):
    template_name = "department/create-department.html"
    form_class = DepartmentAndEmployeeForm
    success_url = reverse_lazy('department:departmentList')

    def form_valid(self, form):
        department = Department.objects.create(
            name=form.cleaned_data['department_name'],
            short_name=form.cleaned_data['department_short_name'],
            active=True
        )

        employee = Employee.objects.create(
            department=department,
            first_name=form.cleaned_data['employee_first_name'],
            last_name=form.cleaned_data['employee_last_name'],
            job=form.cleaned_data['employee_job'],
            avatar=form.cleaned_data['employee_avatar'],
        )

        return super(DepartmentCreateView, self).form_valid(form)
