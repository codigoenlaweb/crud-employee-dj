from django.urls import path
from .views import *

app_name = 'employee'

urlpatterns = [
    path('', prueba.as_view()),
]