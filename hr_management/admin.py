# hr_management/admin.py
from django.contrib import admin
from .models import Employee, Attendance, Leave

admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Leave)
