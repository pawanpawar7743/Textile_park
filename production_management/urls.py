# production_management/urls.py
from django.urls import path
from .views import product_list, work_order_list, create_work_order

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('work-orders/', work_order_list, name='work_order_list'),
    path('create-work-order/', create_work_order, name='create_work_order'),
    # Add other URLs as needed
]







