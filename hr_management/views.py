from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee, Attendance, Leave
from .forms import EmployeeForm, AttendanceForm, LeaveForm

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'hr_management/employee_list.html', {'employees': employees})

@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'hr_management/add_employee.html', {'form': form})

