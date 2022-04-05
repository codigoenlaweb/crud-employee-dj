from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, DeleteView, UpdateView
from .models import Department
from .forms import DepartmentAndEmployeeForm, DepartmentForm
from apps.employee.models import Employee
from django.core.paginator import Paginator


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


class DepartmentDetailView(DetailView):
    model = Department
    template_name = "department/detail-view.html"
    context_object_name = 'department'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        employee_filter = Employee.objects.filter(
            department=kwargs['object'].id)

        paginator = Paginator(employee_filter, 10)

        page_number = self.request.GET.get('page', 1)
        context['employees'] = paginator.get_page(page_number)
        context['range'] = context['employees'].paginator
        return context


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = "department/delete-view.html"
    context_object_name = 'department'
    success_url = reverse_lazy('department:departmentList')



class DepartmentUpdateView(UpdateView):
    model = Department
    template_name = "department/update-view.html"
    form_class = DepartmentForm
    context_object_name = 'department'
    
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        department = form.save()
        self.success_url = reverse_lazy(
            'department:departmentdetail', args=[department.id])
        return super().form_valid(form)