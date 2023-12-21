# production_management/forms.py
from django import forms
from .models import Product, WorkOrder, ProductionRecord

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = '__all__'

class ProductionRecordForm(forms.ModelForm):
    class Meta:
        model = ProductionRecord
        fields = '__all__'

