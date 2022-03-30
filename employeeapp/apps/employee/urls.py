from django.urls import path
from .views import *

app_name = 'employee'

urlpatterns = [
    path('', EmployeeListView.as_view(), name="employeeList"),
    path('<int:pk>', EmployeeDetailView.as_view(), name='employeeshow'),
    path('add employee', EmployeeCreateView.as_view(), name='employeecreate'),
    path('update employee/<int:pk>', EmployeeUpdateView.as_view(), name='employeeupdate'),
    path('delete employee/<int:pk>', EmployeeDeleteView.as_view(), name='employeedelete')
]
