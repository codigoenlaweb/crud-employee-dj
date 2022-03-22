from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('employee', include('apps.employee.urls')),
    path('department', include('apps.department.urls')),
]
