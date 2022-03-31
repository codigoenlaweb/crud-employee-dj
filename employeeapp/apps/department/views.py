from django.shortcuts import render
from django.views.generic import ListView
from .models import Department


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
