# hr_management/urls.py
from django.urls import path
from .views import employee_list, add_employee

urlpatterns = [
    path('employees/', employee_list, name='employee_list'),
    path('add_employee/', add_employee, name='add_employee'),
    # Add more URLs for other views
]

