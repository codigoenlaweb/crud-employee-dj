from django.urls import path
from .views import *

app_name = 'department'

urlpatterns = [
    path('', DepartmentListView.as_view(), name="departmentList"),
    path('add department', DepartmentCreateView.as_view(), name='deparmentcreate'),
]