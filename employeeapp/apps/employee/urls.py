from django.urls import path
from .views import *

app_name = 'employee'

urlpatterns = [
    path('', EmployeeListView.as_view(), name="employeeList"),
]