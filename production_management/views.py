# production_management/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, WorkOrder, ProductionRecord
from .forms import ProductForm, WorkOrderForm, ProductionRecordForm

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'production_management/product_list.html', {'products': products})

@login_required
def work_order_list(request):
    work_orders = WorkOrder.objects.all()
    return render(request, 'production_management/work_order_list.html', {'work_orders': work_orders})

@login_required
def create_work_order(request):
    if request.method == 'POST':
        form = WorkOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('work_order_list')
    else:
        form = WorkOrderForm()
    return render(request, 'production_management/create_work_order.html', {'form': form})

